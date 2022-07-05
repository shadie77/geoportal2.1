// Declare variables 
let form = document.getElementsByClassName('formDetails')[0];
var profileButton = document.getElementById('profileButton');
var jettyButton = document.getElementById('addJettyButton');
var kmlButton = document.getElementById('kmlButton');
var edit = document.getElementById('editButton');
let saveButton = document.getElementById('addData');
let cancel = document.getElementById('cancelEdit');
var layerGroup = L.layerGroup();
let upload = document.getElementById('uploadButton');


/*-------------------------------------------------------------------
SET THE SLIDEOUT COLOR TO BE BLUE WHEN INACTIVE AND WHITE WHEN ACTIVE
----------------------------------------------------------------------*/
function show(openclose) {
    var slideOut = document.getElementsByClassName('mini-info')[0];
    var slideArrow = document.getElementById('slidearrow');
    if (openclose == 'open') {
        if (slideOut.classList.contains('active')) {
            pass
        } else {
            slideOut.classList.toggle('active')
        }

    } else if (openclose == 'close') {
        if (slideOut.classList.contains('active')) {
            slideOut.classList.toggle('active')
        } else {
            pass
        }
    } else {
        slideOut.classList.toggle('active');
    }
    document.getElementsByClassName('jtitle')[0].classList.toggle('active');
    document.getElementsByClassName('content')[0].classList.toggle('active');

    if (slideOut.classList.contains('active')) {
        slideArrow.innerHTML = '»';
        slideArrow.style.color = '#007ee6';
    } else {
        slideArrow.innerHTML = "«";
        slideArrow.style.color = 'white'
    }
}

/* END OF FUNCTION
------------------------------------------------------------------*/

/*------------------------------------------------------------------------------------------
FUNCTION TO ADD JETTY TO DASHBOARD
----------------------------------------------------------------------------------------------*/

addPoint = (e) => {
    // Declare variables
    map.off('click');
    document.getElementById('map').style.cursor = 'crosshair';
    var long = document.getElementById('formLongitude');
    var lat = document.getElementById('formLatitude');
    var jettyName = document.getElementById('jName');
    
    

    kmlButton.disabled = true;
    profileButton.disabled = true;
    jettyButton.disabled = true;
    edit.disabled =false;
    saveButton.disabled = false;
    cancel.disabled = false;

    map.on('click', function(e){
    form.reset();
    console.log(e.latlng.lat);
    long.value = e.latlng.lng;
    lat.value = e.latlng.lat;
    newMarker = new Drift_Marker(e.latlng,{
        draggable: true,
        title: "Resource location",
        alt: "Resource Location",
        riseOnHover: true
    }).bindTooltip('NEW JETTY', {pane: 'tooltipPane', offset: [-3,-12], permanent:true, direction: 'top',  opacity:0.7, className: 'jettylabels'}).openTooltip().addTo(map);
    jettyName.addEventListener('input', updateLabel)
    function updateLabel(){
        newMarker.bindTooltip(this.value);
     }
     newMarker.on("dragend", function (ev) {
        var chagedPos = ev.target.getLatLng();
        long.value = chagedPos.lng;
        lat.value = chagedPos.lat;
      });
     
    // Set the longitude and latitude
    show('open');

    // Keep a record of the form details
    
                      
    form.addEventListener("submit", (e) => {
        e.preventDefault();
        form = document.getElementsByClassName('formDetails')[0];

        myFormData = new FormData(e.target);

        const formDataObj = Object.fromEntries(myFormData.entries());
        newMarker.feature = { 
            type: 'Point', 
            properties: formDataObj, 
            geometry: undefined 
          };
          newMarker.addTo(layerGroup);
          layerGroup.addTo(map);
          console.log(layerGroup);
          // Set the form back to null
          

    });
 
});
}

function cancelEdit() {
    form.reset()
    map.off('click');
    document.getElementById('map').style.cursor = 'grab';
    kmlButton.disabled = false;
    profileButton.disabled = false;
    jettyButton.disabled = false;
    edit.disabled =true;
    saveButton.disabled = true;
    cancel.disabled = true;
    //remove all layers from FeatureGroup
    map.removeLayer(newMarker);
    map.removeLayer(layerGroup);
    show('close');
    layerGroup.clearLayers()


}

function convertToLayer(CSV) {
    var geoLayer = L.geoCsv(CSV, {
        longitudeTitle: 'Long',
        latitudeTitle: 'Lat',
        firstLineTitles: true,
        fieldSeparator: ',',
        pointToLayer: function (feature, latlng) {
            console.log(feature.properties)
            return L.marker(latlng).bindTooltip(feature.properties.name, {pane: 'tooltipPane', offset: [-3,-12], permanent:true, direction: 'top',  opacity:0.7, className: 'jettylabels'}).openTooltip();
    }
    });
    geoLayer.addTo(map);
}

function test(){
    var fileUpload = document.getElementById('myFile');
    if (fileUpload.files.length > 0) {
        var file = fileUpload.files[0];
        var reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
        convertToLayer(evt.target.result);
        saveButton.disabled = false;
        cancel.disabled = false;
        saveButton.addEventListener('click', saveData('csv', evt.target.result));
        }

    }
}

function saveData(filetype, path, params, method='post') {

    // The rest of this code assumes you are not using a library.
    // It can be made less verbose if you use one.
    if (filetype == 'csv'){
        
    }
    const form = document.createElement('form');
    form.method = method;
    form.action = path;
  
    for (const key in params) {
      if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];
  
        form.appendChild(hiddenField);
      }
    }
  
    document.body.appendChild(form);
    form.submit();
  }




function importKML(){
    // Load kml file
    fetch(testkml)
    .then(res => res.text())
    .then(kmltext => {
        // Create new kml overlay
        const parser = new DOMParser();
        const kml = parser.parseFromString(kmltext, 'text/xml');
        const track = new L.KML(kml);
        map.addLayer(track);
        console.log(kml)

    });

}
