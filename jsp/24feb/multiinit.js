
/*
let result = "";


for (let i = 65, j = 97; i <= 90; i++, j++) {
    result += String.fromCharCode(i) + String.fromCharCode(j) + " ";
}

console.log(result.trim());
*/
/*
const output = Array.from({ length: 26 }, (_, k) => {
  const upper = String.fromCharCode(65 + k);
  const lower = String.fromCharCode(97 + k);
  return upper + lower;
}).join(" ");

console.log(output);
*/
/*
const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const result = alphabet
  .split("")
  .map(char => char + char.toLowerCase())
  .join(" ");

console.log(result);
*/
let count = 0;
let finalString = "";

while (count < 26) {
  let upper = String.fromCharCode(65 + count);
  let lower = String.fromCharCode(97 + count);
  
  finalString += `${upper}${lower} `;
  count++;
}

console.log(finalString.trim());