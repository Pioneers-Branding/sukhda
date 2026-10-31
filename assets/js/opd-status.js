/* OPD availability: reads assets/data/opd-status.json and updates the Status
   column. "Edit Availability" lets staff change statuses and download an
   updated opd-status.json, which is then uploaded to assets/data/ on the server. */
(function () {
    var DATA_URL = 'assets/data/opd-status.json';
    var STATUS = {
        available: { cls: 'available', icon: 'check-circle', label: 'Doctor Available' },
        unavailable: { cls: 'unavailable', icon: 'x-circle', label: 'Doctor Not Available' },
        oncall: { cls: 'oncall', icon: 'phone-incoming', label: 'On Call' }
    };

    var rows = document.querySelectorAll('.opd-row[data-doctor]');
    if (!rows.length) return;

    var state = { updated: '', doctors: {} };

    // Seed from the statuses already written in the HTML (used if the JSON can't load).
    rows.forEach(function (row) {
        var badge = row.querySelector('[data-status-badge]');
        var name = row.querySelector('.opd-doc-name');
        var status = 'available';
        if (badge && badge.classList.contains('oncall')) status = 'oncall';
        if (badge && badge.classList.contains('unavailable')) status = 'unavailable';
        state.doctors[row.getAttribute('data-doctor')] = {
            name: name ? name.textContent.trim() : row.getAttribute('data-doctor'),
            status: status,
            note: ''
        };
    });

    function esc(t) {
        var d = document.createElement('div');
        d.textContent = t;
        return d.innerHTML;
    }

    function refreshIcons() {
        if (window.lucide) lucide.createIcons();
    }

    function render() {
        rows.forEach(function (row) {
            var info = state.doctors[row.getAttribute('data-doctor')];
            var badge = row.querySelector('[data-status-badge]');
            if (!info || !badge) return;
            var st = STATUS[info.status] || STATUS.available;
            badge.className = 'status-badge ' + st.cls;
            badge.innerHTML = '<i data-lucide="' + st.icon + '" style="width:11px;height:11px"></i> ' + st.label;
            row.classList.toggle('is-unavailable', info.status === 'unavailable');

            var cell = badge.parentNode;
            var note = cell.querySelector('.status-note');
            if (info.note) {
                if (!note) {
                    note = document.createElement('small');
                    note.className = 'status-note';
                    cell.appendChild(note);
                }
                note.textContent = info.note;
            } else if (note) {
                note.remove();
            }
        });

        var upd = document.getElementById('opdStatusUpdated');
        if (upd && state.updated) {
            var d = new Date(state.updated + 'T00:00:00');
            upd.textContent = 'Last updated: ' + (isNaN(d) ? state.updated :
                d.toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' }));
            upd.hidden = false;
        }
        refreshIcons();
    }

    // ---------- Edit mode ----------
    var bar = document.getElementById('opdEditBar');
    var toggle = document.getElementById('opdEditToggle');

    function openEditor() {
        if (bar) bar.hidden = false;
        if (toggle) toggle.hidden = true;
        rows.forEach(function (row) {
            var key = row.getAttribute('data-doctor');
            var info = state.doctors[key];
            var cell = row.querySelector('[data-status-badge]').parentNode;
            if (cell.querySelector('.status-editor')) return;
            var box = document.createElement('div');
            box.className = 'status-editor';
            box.innerHTML =
                '<select aria-label="Status for ' + esc(info.name) + '">' +
                Object.keys(STATUS).map(function (k) {
                    return '<option value="' + k + '"' + (k === info.status ? ' selected' : '') + '>' + STATUS[k].label + '</option>';
                }).join('') +
                '</select>' +
                '<input type="text" maxlength="80" placeholder="Note (optional), e.g. On leave till 5 Nov" value="' + esc(info.note || '') + '">';
            box.querySelector('select').addEventListener('change', function (e) {
                info.status = e.target.value;
                render();
            });
            box.querySelector('input').addEventListener('input', function (e) {
                info.note = e.target.value.trim();
                render();
            });
            cell.appendChild(box);
        });
    }

    function closeEditor() {
        if (bar) bar.hidden = true;
        if (toggle) toggle.hidden = false;
        document.querySelectorAll('.status-editor').forEach(function (el) { el.remove(); });
    }

    function download() {
        var now = new Date();
        state.updated = now.getFullYear() + '-' + String(now.getMonth() + 1).padStart(2, '0') + '-' + String(now.getDate()).padStart(2, '0');
        render();
        var blob = new Blob([JSON.stringify(state, null, 2) + '\n'], { type: 'application/json' });
        var a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'opd-status.json';
        document.body.appendChild(a);
        a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    }

    if (toggle) toggle.addEventListener('click', openEditor);
    var cancel = document.getElementById('opdEditCancel');
    if (cancel) cancel.addEventListener('click', closeEditor);
    var dl = document.getElementById('opdEditDownload');
    if (dl) dl.addEventListener('click', download);

    // ---------- Load published statuses ----------
    fetch(DATA_URL, { cache: 'no-store' })
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (json) {
            if (!json || !json.doctors) return;
            if (json.updated) state.updated = json.updated;
            Object.keys(json.doctors).forEach(function (k) {
                if (state.doctors[k]) {
                    state.doctors[k].status = STATUS[json.doctors[k].status] ? json.doctors[k].status : 'available';
                    state.doctors[k].note = json.doctors[k].note || '';
                    if (json.doctors[k].name) state.doctors[k].name = json.doctors[k].name;
                }
            });
        })
        .catch(function () { })
        .then(function () {
            render();
            if (/[?&]edit=1\b/.test(location.search)) openEditor();
        });
})();
