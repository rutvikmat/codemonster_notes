// --- Number Precision & EPSILON ---
let x = Number.EPSILON;
console.log(x);

console.log(0.1 + 0.2 === 0.3);
console.log(Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON);