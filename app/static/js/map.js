/* Global map object, we can write functions to do stuff to this guy */
var map;
var placementMode = false;

function initMap() {
  var initialLoc;
  if (allPins.length == 0) {
    initialLoc = {lat: 42.3241, lng: -72.5307};
  } else {
    var lastPin = allPins[allPins.length-1];
    initialLoc = {lat: lastPin.lat, lng: lastPin.lng};
  }
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: initialLoc,
    disableDefaultUI: true
  });
  google.maps.event.addListener(map, 'click', function(event) {
     if (placementMode) createPin(event.latLng);
  });
  if(typeof(lat_input) !== null && typeof(lat_input) !== 'undefined' && typeof(lng_input) !== null && typeof(lng_input) !== 'undefined'){
      displayOnePin(latLng.lat, latLng.lng);
  }
  placeAllMarkers(allPins);
}

function createPin(location) {
  enterPinForm(location.toJSON());
}

function placeMarker(pin) {
  var latLng = {lat: pin.lat, lng: pin.lng};
  var title = '<h5>' + pin.name + '</h5><br />';
  var sign = '<div class="chip">' + pin.user_email + '</div><br />';
  var description = '<div class="info-window-description"><h6>' + pin.description + '</h6></div>';
  var infowindow = new google.maps.InfoWindow({
    content: title + description + sign
  });
  var marker = new google.maps.Marker({
      position: latLng,
      map: map
  });
  marker.addListener('click', function() {
    infowindow.open(map, marker);
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
    map.panTo(latLng);
    var marker = new google.maps.Marker({
        position: latLng,
        map: map
    });
}

function placeAllMarkers(pins){
    for(i=0; i<pins.length; i++){
        placeMarker(pins[i]);
    }
}

function enterPinForm(location) {
  $('#form_lat').val(location.lat);
  $('#form_lng').val(location.lng);
  $('#modal1').modal('open');
}
