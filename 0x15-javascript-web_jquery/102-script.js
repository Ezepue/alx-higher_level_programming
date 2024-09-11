// script that fetches and prints how to say “Hello” depending on the language
$(document).ready(() => {
  // add click event listener
  $('INPUT#btn_translate').click(() => {
    // Extract input
    const langCode = $('INPUT#language_code').val();
    // Fetch hello using language
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, (data) => {
      const hello = data.hello;
      // Display tanslation
      $('DIV#hello').text(hello);
    });
  });
});
