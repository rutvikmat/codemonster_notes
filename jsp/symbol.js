let sym1 = Symbol("id");
let sym2 = Symbol("id");

console.log(sym1 === sym2);

let id = Symbol("id");

let user = {
    name: "rutvik",
    age: 25,
    [id]: 105
};

console.log(user.name);
console.log(user[id]);


let big = BigInt(12345678901234567890);
console.log(big);

let big1 = 9007199254740991n;
let big2 = 2n;
console.log(typeof big1)