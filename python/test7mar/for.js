let num = 1234;
let sum = 0;

for (num ; num > 0; num = Math.floor(num / 10)) {
    let digit = num % 10;
    sum += digit;
}

console.log("Sum of digits:", sum);