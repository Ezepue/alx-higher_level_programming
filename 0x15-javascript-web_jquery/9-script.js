// Script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(() => {
  // Get the value of hello from url
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    const helloVal = data.hello;
    $('DIV#hello').text(helloVal);
  });
});
