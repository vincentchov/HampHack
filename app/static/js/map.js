function initMap() {
    var hampshireCollege = {lat: 42.3241, lng: -72.5307};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: hampshireCollege
    });
    var marker = new google.maps.Marker({
      position: hampshireCollege,
      map: map
    });
  }
