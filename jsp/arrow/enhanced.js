const name = "Skywalker";
const rank = "Jedi";

// Old way: { name: name, rank: rank }
// New way (Shorthand):
const pilot = { name, rank }; 

console.log(pilot); // { name: "Skywalker", rank: "Jedi" }
