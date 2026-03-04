// --- Math Methods ---
console.log(Math.trunc(4.9));
console.log(Math.trunc(-4.9));

console.log(Math.sign(10));
console.log(Math.sign(-5));
console.log(Math.sign(0));

console.log(Math.cbrt(27));
console.log(Math.cbrt(8));

console.log(Math.log2(8));
console.log(Math.log2(16));

console.log(Math.log10(100));
console.log(Math.log10(1000));

// --- Number Precision & EPSILON ---
let x = Number.EPSILON;
console.log(x);

console.log(0.1 + 0.2 === 0.3);
console.log(Math.abs((0.1 + 0.2) - 0.3) < Number.EPSILON);

// --- Safe Integer Limits ---
console.log(Number.MIN_SAFE_INTEGER);
console.log(Number.MAX_SAFE_INTEGER);

// --- Number Validation Methods ---
console.log(Number.isInteger(10));
console.log(Number.isInteger(10.5));
console.log(Number.isInteger("10"));

console.log(Number.isSafeInteger(100));
console.log(Number.isSafeInteger(9007199254740991));
console.log(Number.isSafeInteger(9007199254740992));

// --- Global Utility Methods ---
console.log(isFinite(10 / 0));
console.log(isFinite(10 / 1));
console.log(isFinite("10"));

console.log(isNaN("Hello"));
console.log(isNaN("10"));
console.log(isNaN(10));