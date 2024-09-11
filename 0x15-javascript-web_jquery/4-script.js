// Toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header
$(document).ready(() => {
  // Add click listener on DIV#toggle_header
  $('DIV#toggle_header').click(() => {
    // Toggle <header> class
    $('header').toggleClass('red green');
  });
});
