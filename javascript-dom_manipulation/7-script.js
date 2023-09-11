/*
Write a JavaScript script that fetches and lists the title
for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML ul element with id list_movies
You must use the Fetch API.
*/
const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
const id = document.getElementById('list_movies');

fetch(URL)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const films = data.results;
    for (let i = 0; i < films.length; i++) {
      const li = document.createElement('li');
      li.textContent = films[i].title;
      id.appendChild(li);
    }
  });
