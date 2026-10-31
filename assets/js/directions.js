/* Get Directions links: open Google Maps navigation and, on mobile, show the
   approximate (straight-line) distance from the visitor to the hospital.
   Any element with data-directions-lat / data-directions-lng gets a distance
   written into its .dir-km child once the visitor's location is known. */
(function () {
    var targets = document.querySelectorAll('[data-directions-lat][data-directions-lng]');
    if (!targets.length || !('geolocation' in navigator)) return;

    var isMobile = window.matchMedia('(max-width: 900px)').matches ||
        /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

    function km(lat1, lng1, lat2, lng2) {
        var r = Math.PI / 180, R = 6371;
        var dLat = (lat2 - lat1) * r, dLng = (lng2 - lng1) * r;
        var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
            Math.cos(lat1 * r) * Math.cos(lat2 * r) * Math.sin(dLng / 2) * Math.sin(dLng / 2);
        return 2 * R * Math.asin(Math.sqrt(a));
    }

    function show(pos) {
        targets.forEach(function (el) {
            var lat = parseFloat(el.getAttribute('data-directions-lat'));
            var lng = parseFloat(el.getAttribute('data-directions-lng'));
            var out = el.querySelector('.dir-km');
            if (isNaN(lat) || isNaN(lng) || !out) return;
            var d = km(pos.coords.latitude, pos.coords.longitude, lat, lng);
            out.textContent = '≈ ' + (d < 10 ? d.toFixed(1) : Math.round(d)) + ' km away';
            out.hidden = false;
        });
    }

    function locate() {
        navigator.geolocation.getCurrentPosition(show, function () { }, {
            enableHighAccuracy: false, timeout: 10000, maximumAge: 600000
        });
    }

    // Desktop: only when permission was already granted (never prompt).
    // Mobile: ask once after the page has loaded.
    if (navigator.permissions && navigator.permissions.query) {
        navigator.permissions.query({ name: 'geolocation' }).then(function (p) {
            if (p.state === 'granted' || (isMobile && p.state === 'prompt')) {
                setTimeout(locate, 1500);
            }
        }).catch(function () { if (isMobile) setTimeout(locate, 1500); });
    } else if (isMobile) {
        setTimeout(locate, 1500);
    }
})();
