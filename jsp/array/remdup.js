const numbers = [1, 2, 2, 3, 4, 4, 5];

// Convert to Set (which ignores duplicates) and back to Array
const uniqueNumbers = [...new Set(numbers)];

console.log(uniqueNumbers);