/* OPD availability: reads assets/data/opd-status.json and updates the Status column. */
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
        });
})();
