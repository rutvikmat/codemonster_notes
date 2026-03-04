const ids = new Set([1, 2, 2, 3, 4, 4]);

console.log(ids); // Set(4) {1, 2, 3, 4}
ids.add(5);       // Adds 5
ids.delete(1);    // Removes 1