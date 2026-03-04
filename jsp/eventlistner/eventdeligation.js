const list = document.querySelector('#parent-list');

list.addEventListener('click', (event) => {
  // Check if the clicked element is actually a list item
  if (event.target.tagName === 'LI') {
    console.log(`You clicked on: ${event.target.innerText}`);
  }
});