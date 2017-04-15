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
        position: hampshireCollege,
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

function displayOnePin(latLng) {
    if(typeof(latLng) === 'object' && isFloat(latLng['lat']) && isFloat(latLng['lng'])){
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 15,
            center: latLng,
            disableDefaultUI: true
        });
        var marker = new google.maps.Marker({
            position: latLng,
            map: map
        });
    }
}
