const searchBar = document.querySelector('#search');

searchBar.addEventListener('input', (event) => {
  // event.target.value gets the current text in the box
  console.log(`User is typing: ${event.target.value}`);
});