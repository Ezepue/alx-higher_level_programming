// adds the class red to the <header> element when the user clicks on the tag DIV#red_header
$(document).ready(() => {
  // Add click listiner to DIV#red_header
  $('DIV#red_header').click(() => {
    // Add class red tp the <header> element
    $('header').addClass('red');
  });
});
