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
}

function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
    enterPinForm();
}

function togglePlacementMode() {
  placementMode = !placementMode;
}

function enterPinForm() {
  console.log('Hello');
  $('#modal1').modal('open');
}
