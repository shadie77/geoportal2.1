
addPoint = (e) => {
    document.getElementsByName('body');
    map.on('click', function(e){
    var newMarker = new L.marker(e.latlng).addTo(map);
    show()
});
}