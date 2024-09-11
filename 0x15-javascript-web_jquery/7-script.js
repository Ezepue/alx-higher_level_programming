// Script that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    // Extract Character Name
    const characterName = data.name;

    // Update content of the <div id="character"> with characterName
    $('DIV#character').text(characterName);
  });
});
