// Script that fetches  fetches and lists the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json
$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    // Iterate through each movie in response
    $.each(data.results, (index, movie) => {
      // Extract Character Name
      const movieTitle = movie.title;
      // Create new movie list iten with movie title
      const listItem = $('<li>').text(movieTitle);
      // Update content of the <div id="character"> with movieTitle
      $('UL#list_movies').append(listItem);
    });
  });
});
