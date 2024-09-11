// Adds a <li> element to a list when the user clicks on the tag DIV#add_item
$(document).ready(() => {
  // Add a click event listener
  $('DIV#add_item').click(() => {
    $('<li>').text('Item').appendTo('UL.my_list');
  });
});
