var name = "John";
var name = "Doe"; // No error! This can cause bugs.

if (true) {
    var status = "Active"; 
}
console.log(status); // "Active" - var leaked out of the IF block!