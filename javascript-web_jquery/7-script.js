/*
Write a JavaScript script that fetches the character name
from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
The name must be displayed in the HTML tag DIV#character
*/

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
	$('#character').text(data.name)
  });
  