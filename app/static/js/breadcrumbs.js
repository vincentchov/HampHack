$(document).ready(function() {
  /* Setup event listeners */
  $('#add-pin').click(enterPlacementMode);
})

function enterPlacementMode() {
  if (placementMode) {
    $('#add-pin-icon').html('add');
  } else {
    $('#add-pin-icon').html('close');
  }
  togglePlacementMode();
}
