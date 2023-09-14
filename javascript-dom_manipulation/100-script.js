/*
Write a JavaScript script that adds, removes and clears li elements from a list when the user clicks:
The new element must be: <li>Item</li>
The new element must be added to the element with id my_list
When the user clicks on the element with id add_item: a new element is added to the list
When the user clicks on the element with id remove_item: the last element is removed from the list
When the user clicks on the element with id clear_list: all elements of the list are removed You 
script must work when it imported from the head tag Please test with this HTML file in your browser
*/

document.addEventListener("DOMContentLoaded", (event) => {
  const addItem = document.querySelector("#add_item");
  const deleteItem = document.querySelector("#remove_item");
  const clearList = document.querySelector("#clear_list");
  const myList = document.querySelector(".my_list");

  addItem.addEventListener("click", () => {
    const doc = document.createElement("li");
    doc.textContent = "Item";
    myList.appendChild(doc);
  });

  deleteItem.addEventListener("click", () => {
    const element = myList.querySelector("li:last-child");
    if (element) {
      element.remove();
    }
  });

  clearList.addEventListener("click", () => {
    const elements = myList.querySelectorAll("li");
    elements.forEach((element) => {
      element.remove();
    });
  });
});
