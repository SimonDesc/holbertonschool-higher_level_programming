/*
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://hellosalut.stefanbohacek.dev/
The language code will be the value selected in the combo box with id language_code (es, fr, en etc.)
The translation must be fetched when the user clicks on element with id btn_translate
The translation of “Hello” must be displayed in the HTML tag with id hello
You script must work when imported from the <head> tag
*/

document.addEventListener("DOMContentLoaded", (event) => {
  const helloDiv = document.querySelector("#hello");
  const createLi = document.createElement("li");
  const selectLanguage = document.querySelector("#language_code");
  const buttonTranslate = document.querySelector("#btn_translate");

  buttonTranslate.addEventListener("click", (event) => {
    const index = selectLanguage.value;

    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${index}`)
      .then((response) => {
        return response.json();
      })
      .then((jsonData) => {
        createLi.textContent = jsonData.hello;
        helloDiv.appendChild(createLi);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
