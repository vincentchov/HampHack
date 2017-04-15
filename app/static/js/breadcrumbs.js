$(document).ready(function() {
  $('.tap-target').tapTarget('open');
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
    $('#add-pin-icon').html('close');
    $('#cancel-drop').show('slide', { direction: 'right' }, 250);
  }
  togglePlacementMode();
}
