// --- Number Validation Methods ---
console.log(Number.isInteger(10));
console.log(Number.isInteger(10.5));
console.log(Number.isInteger("10"));

console.log(Number.isSafeInteger(100));
console.log(Number.isSafeInteger(9007199254740991));
console.log(Number.isSafeInteger(9007199254740992));