const toggleAddItem = document.getElementById("add_item");
const myList = document.getElementsByClassName("my_list");

toggleAddItem.addEventListener("click", function () {
  console.log(myList);
  for (let i = 0; i < myList.length; i++) {
    let li = document.createElement("li");
    li.textContent = "Item";
    myList[i].appendChild(li);
  }
});
