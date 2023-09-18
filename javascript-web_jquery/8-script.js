/*
Write a JavaScript script that fetches and lists the title for all
movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
*/

$.get("https://swapi-api.hbtn.io/api/films/?format=json", function (data) {
  list = data.results;

  for (let i = 0; i < list.length; i++) {
    console.log(list[i].title);
    $("#list_movies").append("<li>" + list[i].title + "</li>");
  }
});
