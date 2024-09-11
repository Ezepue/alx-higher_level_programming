// updates the text color of the <header> element to red (#FF0000)
// when the user clicks on the tag DIV#red_header.
$(document).ready(() => {
  // Add click listener
  $('DIV#red_header').click(() => {
    // Update header color
    $('header').css('color', '#FF0000');
  });
});
