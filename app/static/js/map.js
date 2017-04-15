/* Global map object, we can write functions to do stuff to this guy */
var map;
var placementMode = false;

function initMap() {
  var hampshireCollege = {lat: 42.3241, lng: -72.5307};
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: hampshireCollege,
    disableDefaultUI: true
  });
  google.maps.event.addListener(map, 'click', function(event) {
     if (placementMode) placeMarker(event.latLng);
  });
  if(typeof(lat_input) !== null && typeof(lat_input) !== 'undefined' && typeof(lng_input) !== null && typeof(lng_input) !== 'undefined'){
      displayOnePin(latLng.lat, latLng.lng);
  }
  placeAllMarkers(allPins);
}

function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

function togglePlacementMode() {
  placementMode = !placementMode;
// Used to check if an inputted LatLng object is valid
}

function isFloat(n){
    return Number(n) === n && n % 1 !== 0;
}


function displayOnePin(lat_input, lng_input) {
    var latLng = {lat: lat_input, lng: lng_input};
    map.setCenter(latLng);
    var marker = new google.maps.Marker({
        position: latLng,
        map: map
    });
}

function placeAllMarkers(pins){
    for(i=0; i<pins.length; i++){
        var latLng = {lat: pins[i].lat, lng: pins[i].lng};
        placeMarker(latLng);
    }
}
