const employee = {
    empId: 101,
    firstName: "Amit",
    lastName: "Sharma",
    salary: 50000,
    work() {
        console.log('Working...');
    }
};

// --- Method 1: The Spread Operator (Recommended) ---
// This is the cleanest and most modern way.
const clone1 = { ...employee };
console.log("Clone via Spread:", clone1);


// --- Method 2: Object.assign() ---
// Great if you want to add new properties while cloning.
const clone2 = Object.assign({
    dept: 'IT',
    location: 'Bangalore'
}, employee);
console.log("Clone via Assign:", clone2);


// --- Method 3: for...in Loop ---
// The manual way (how things were done in older JS).
const clone3 = {};
for (let key in employee) {
    clone3[key] = employee[key];
}
console.log("Clone via Loop:", clone3);