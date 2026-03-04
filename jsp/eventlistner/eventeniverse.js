function welcome() {
  console.log('Hello!');
}

const box = document.querySelector('.box');

// Add it
box.addEventListener('mouseover', welcome);

// Remove it after 5 seconds
setTimeout(() => {
  box.removeEventListener('mouseover', welcome);
}, 5000);