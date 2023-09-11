const toggleAddItem = document.getElementById('add_item');
const myList = document.querySelectorAll('.my_list');

toggleAddItem.addEventListener('click', () => {
  myList.forEach(element => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    element.appendChild(li);
  });
});
