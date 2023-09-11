/*
Write a JavaScript script that fetches from
https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML element with id hello.

The translation of “hello” must be displayed in the HTML element with id hello
Your script must work when it is imported from the <head> tag
*/

document.addEventListener('DOMContentLoaded', (event) => {
  const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const id = document.querySelector('#hello');

  fetch(URL)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const p = document.createElement('p');
      p.textContent = data.hello;
      id.appendChild(p);
    });
});
