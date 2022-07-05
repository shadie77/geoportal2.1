
function map_init_basic(map, options) {
      var jetty_url = "http://127.0.0.1:8000/api/jetty";
      var route_url = "http://127.0.0.1:8000/api/route";
      var depth_url = 'http://127.0.0.1:8000/api/depth';
      var jettyLayer = new L.GeoJSON.AJAX(jetty_url,{
              onEachFeature: function onEachFeature(feature, layer) {
                var props = feature.properties;
                var content = `<img width="300" src="${props.picture_url}"/><h3>${props.name}</h3><p>${props.terminal}</p>`;
                layer.bindPopup(content);
                layer.on("click", function(e){
                  document.getElementsByClassName('laswaside')[1].click();
                } );
      }
    });
jettyLayer.addTo(map).on('click', function(e) { console.log(e.layer) });
var routeLayer = new L.GeoJSON.AJAX(route_url,{
        
      });
      routeLayer.addTo(map);
    var depthLayer = new L.GeoJSON.AJAX(depth_url,{
        
    });
    depthLayer.addTo(map);
    }