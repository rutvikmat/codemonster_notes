let character = "e"; 
let letter = character.toLowerCase(); 

switch (letter) {
  case 'a':
  case 'e':
  case 'i':
  case 'o':
  case 'u':
    console.log(`${character} is a vowel. `);
    break;

  default:
    console.log(`${character} is a consonant. `);
    break;
}