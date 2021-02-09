function createMap(id) {
    var map = L.map(id, {
        scrollWheelZoom: false
    });
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    return map;
}

function addGroundStation(map, lat, lon, text="GroundStation") {
    return L.circleMarker([lat, lon], {
        radius: 6.0,
        fillColor: '#11fe00',
        weight: 1,
        opacity: 1.0,
        fillOpacity: 0.8
    }).addTo(map).bindPopup(text);
}

function addSatelliteTrack(map, track) {
    var polyline = L.polyline(track , {color: 'red'}).addTo(map);
    
    L.circleMarker(track[0], {
      radius: 4.0,
      fillColor: '#000000',
      weight: 1,
      opacity: 1.0,
      fillOpacity: 0.8
    }).addTo(map).bindPopup("start");
    
    L.circleMarker(track[track.length - 1], {
      radius: 4.0,
      stroke: true,
      color: '#000000',
      weight: 3,
      fillColor: '#FFFFFF',
      weight: 1,
      opacity: 1.0,
      fillOpacity: 0.8
    }).addTo(map).bindPopup("end");
    
    map.fitBounds(polyline.getBounds());
}

function getGroundTrackOfTle(tle, start, end) {
    var step  = 30; // in sec
    var track = [];

    var satrec = satellite.twoline2satrec(tle[0], tle[1]);

    for (var i = start; i < end; i += step) {
        var time = new Date(i * 1000);

        var positionEci = satellite.propagate(satrec, time).position;
        var gmst        = satellite.gstime(time);
        var positionGd  = satellite.eciToGeodetic(positionEci, gmst);
        
        track.push([
            satellite.degreesLat(positionGd.latitude),
            satellite.degreesLong(positionGd.longitude)
        ]);
    }

    return track
}

function loadTle(id) {
    return [
        document.getElementById(id).getAttribute("line2"),
        document.getElementById(id).getAttribute("line3")
    ]
}
