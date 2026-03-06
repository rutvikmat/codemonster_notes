let numbers = [10, 20, 30, 40];

for (let value of numbers) {
    console.log(value);
}

let name = "Pavitra";

for (let ch of name) {
    console.log(ch);
}

let mySet = new Set([1, 2, 3]);

for (let item of mySet) {
    console.log(item);
}

let map = new Map([
    ["name", "Avanija"],
    ["age", 10]
]);

for (let entry of map) {
    console.log(entry);
}

for (let [key, value] of map) {
    console.log(key + " : " + value);
}