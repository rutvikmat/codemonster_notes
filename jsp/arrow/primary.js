function double(n) {
  return n * 2;
}


const double = (n) => n * 2;


// no parameters
const sayHello = () => console.log("Hello World!");
sayHello();


// shorthand 
const square = x => x * x;
console.log(square(5)); // 25

// multiple parameter 
const area = (length, width) => length * width;
console.log(area(10, 5)); // 50


// Implicit
const add = (a, b) => a + b;

// Explicit
const multiplyAndLog = (a, b) => {
  const result = a * b;
  console.log("Result is:", result);
  return result; 
};


// returning object 
const getUser = (id) => ({ id: id, role: "Admin" });
console.log(getUser(101)); // {id: 101, role: "Admin"}
