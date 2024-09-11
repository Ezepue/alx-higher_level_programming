/* Script that adds, removes and clears LI elements from a list when the user clicks:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
When the user clicks on DIV#add_item: a new element is added to the list
When the user clicks on DIV#remove_item: the last element is removed from the list
When the user clicks on DIV#clear_list: all elements of the list are removed
*/
$(document).ready(() => {
  // Add a click event listener for DIV#add_item
  $('DIV#add_item').click(() => {
    // Add new LI element
    const liElement = $('<li>').text('Item');
    $('UL.my_list').append(liElement);
  });
  // Add a click event listener for DIV#remove_item
  $('DIV#remove_item').click(() => {
    // remove last li element
    $('UL.my_list li:last-child').remove();
  });
  // Add a click event listener for DIV#clear_list
  $('DIV#clear_list').click(() => {
    // Remove all LI elements
    $('UL.my_list').empty();
  });
});
