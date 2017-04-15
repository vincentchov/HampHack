$(document).ready(function() {
  /* Setup event listeners */
  $('#add-pin').click(enterPlacementMode);
})

function enterPlacementMode() {
  if (placementMode) {
    $('#add-pin-icon').html('add_location');
    $('.toast').remove();
    $('#cancel-drop').hide();
  } else {
    Materialize.toast('Click anywhere to drop a pin', 4000);
    $('#cancel-drop').show();
    $('#add-pin-icon').html('close');
  }
  togglePlacementMode();
}
