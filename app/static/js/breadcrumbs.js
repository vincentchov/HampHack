$(document).ready(function() {
  /* Setup event listeners */
  $('#add-pin').click(enterPlacementMode);
})

function enterPlacementMode() {
  if (placementMode) {
    $('#add-pin-icon').html('add_location');
    $('#cancel-drop').hide('slide', { direction: 'right' }, 250);
    $('.toast').remove();
  } else {
    Materialize.toast('Click anywhere to drop a pin', 4000);
    $('#cancel-drop').show('slide', { direction: 'right' }, 250);
    $('#add-pin-icon').html('close');
  }
  togglePlacementMode();
}
