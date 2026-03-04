let variable = 3; 

console.log("--- Language Menu ---");
console.log("1 - English");
console.log("2 - Hindi");
console.log("3 - Kannada");
console.log("4 - Tamil");
console.log("5 - Telugu");
console.log("---------------------");

switch(variable) {
    case 1:
        console.log("Output: You selected English");
        break;
    case 2:
        console.log("Output: You selected Hindi");
        break;
    case 3:
        console.log("Output: You selected Kannada");
        break;
    case 4:
        console.log("Output: You selected Tamil");
        break;
    case 5:
        console.log("Output: You selected Telugu");
        break;
    default:
        console.log("Output: Invalid selection");
        break;
}