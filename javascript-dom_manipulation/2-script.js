// Write a JavaScript script that adds the
// class red to the header element when the user clicks on the tag with id red_header
const titre = document.getElementById('red_header');
const firstTitre = document.querySelector('header');
titre.addEventListener('click', () => {
  firstTitre.classList.toggle('red');
});
