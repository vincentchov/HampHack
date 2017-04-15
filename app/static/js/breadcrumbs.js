$(document).ready(function() {
  $('.tap-target').tapTarget('open');
  /* Setup event listeners */
  $('#add-pin').click(enterPlacementMode);
});

$(document).ready(function(){
   // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
   $('.modal').modal();
 });

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
