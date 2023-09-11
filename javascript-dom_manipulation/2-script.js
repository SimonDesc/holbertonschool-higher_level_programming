const titre = document.getElementById('red_header');
const firstTitre = document.querySelector('header');
titre.addEventListener('click', function () {
  firstTitre.classList.add('red');
});
