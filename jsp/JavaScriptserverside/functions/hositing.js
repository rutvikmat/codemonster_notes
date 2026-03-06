//Variable Hoisting with var
console.log(name); // Output: undefined (instead of an error!)
var name = "rutvik";
console.log(name); // Output: "Gemini"


var name;           // Declaration is hoisted to the top
console.log(name);  // It exists, but has no value yet
name = "rutvik";    // Assignment stays in place


/*
//Variable Hoisting with let and const
console.log(age); // ReferenceError: Cannot access 'age' before initialization
let age = 25;
*/

//Function Hoisting
sayHello(); // Output: "Hello there!"

function sayHello() {
  console.log("Hello there!");
}