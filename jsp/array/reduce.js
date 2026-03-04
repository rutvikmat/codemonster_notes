const cart = [5, 15, 10];

// Summing up the total
const total = cart.reduce((accumulator, current) => {
  return accumulator + current;
}, 0); 

console.log(total); 