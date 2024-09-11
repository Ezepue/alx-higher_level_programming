// script that fetches and prints how to say “Hello” depending on the language
$(document).ready(() => {
  // Translator function
  function fetchTranslation () {
    // Extract input
    const langCode = $('INPUT#language_code').val();
    // Fetch hello using language
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, (data) => {
      const hello = data.hello;
      // Display tanslation
      $('DIV#hello').text(hello);
    });
  }
  // add click event listener to translate button
  $('INPUT#btn_translate').click(fetchTranslation);
  // Add keyup event listener to input field for enter key
  $('INPUT#language_code').keyup((event) => {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
