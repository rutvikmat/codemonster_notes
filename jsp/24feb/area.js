function calculateCircleArea(radius) {
  return Math.PI * (radius ** 2);
}

function calculateRectangleArea(length, width) {
  return length * width;
}

function calculateSquareArea(side){
    return side * side;
}

let shape = "squre"; 
let radius = 7;
let length = 10;
let width = 5;
let side = 4;

switch (shape) {
    case "circle":
        let cArea = calculateCircleArea(radius);
        console.log(`Circle Area: ${cArea.toFixed(2)}`);
        break;

    case "rectangle":
        let rArea = calculateRectangleArea(length, width);
        console.log(`Rectangle Area: ${rArea}`);
        break;

    case "squre":
        let rSquare = calculateSquareArea(side);
        console.log(`Area Of sqaure : ${rSquare}`);
        break;

    default:
        console.log("Unknown shape selected.");
        break;
}