const userRoles = new Map();

userRoles.set("admin", "Alice");
userRoles.set(1, "Bob"); // Number as a key!

console.log(userRoles.get(1)); // "Bob"
console.log(userRoles.size);   // 2