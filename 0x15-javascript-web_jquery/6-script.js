// Script that updates the text of the <header> element
// to New Header!!! when the user clicks on DIV#update_header
$(document).ready(() => {
  // Add click listener to DIV#update_header
  $('DIV#update_header').click(() => {
    // Update text of <header> to 'New Header!!!'
    $('header').text('New Header!!!');
  });
});
