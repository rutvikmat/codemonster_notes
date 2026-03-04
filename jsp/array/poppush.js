const fruits = ["Apple", "Banana"];
console.log(fruits);
fruits.push("Orange"); 
fruits.pop();

// var
var name = "John";
var name = "Doe"; // No error! This can cause bugs.

if (true) {
    var status = "Active"; 
}
console.log(status); // "Active" - var leaked out of the IF block!
// .forEach()
const prices = [100, 200, 300];
prices.forEach(price => console.log(`Price Tag: $${price}`));

// ,find()
const users = [{id: 1, name: "Avi"}, {id: 2, name: "Sam"}];
const user = users.find(u => u.id === 2); // Returns the object for Sam

// .some() and .every()
const marks = [80, 45, 90];
const hasFailed = marks.some(m => m < 50); // true



// splicing and slicing
const colors = ["Red", "Green", "Blue", "Yellow"];
const middleColors = colors.slice(1, 3); // ["Green", "Blue"]



// events //
// click
const btn = document.querySelector('#submitBtn');
btn.addEventListener('click', () => alert("Form Submitted!"));

// input
const input = document.querySelector('input');
input.addEventListener('input', (e) => {
  console.log("Current typing:", e.target.value);
});

// Mouseover & Mouseleave
const box = document.querySelector('.box');
box.addEventListener('mouseover', () => box.style.backgroundColor = 'red');
box.addEventListener('mouseleave', () => box.style.backgroundColor = 'blue');

// Keydown 
window.addEventListener('keydown', (e) => {
  if (e.key === "Enter") console.log("User hit Enter!");
});

// submit
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  e.preventDefault(); // Stops page reload
  console.log("Processing data...");
});
