
// Example map.js content for Leaflet.js
document.addEventListener("DOMContentLoaded", function () {

    var map = L.map('map').setView([43.95, -79.7], 7);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiY3ludGhpYWwiLCJhIjoiY2x0b3FjNXUyMGh6eTJqcGF4MWllYjh0eCJ9.OHUn3IOjS99GIMLYMmyh4w', {
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);
        
    function onMapClick(e) {
        document.getElementById('latitude').value = e.latlng.lat;
        document.getElementById('longitude').value = e.latlng.lng;
    }

    map.on('click', onMapClick);
});

