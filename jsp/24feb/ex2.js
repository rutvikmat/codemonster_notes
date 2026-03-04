let number = -5;
let type;

if (number > 0) {
  type = "positive";
} else if (number < 0) {
  type = "negative";
} else {
  type = "zero";
}

switch (type) {
  case "positive":
    console.log(" number is positive.");
    break;
  case "negative":
    console.log("number is negative.");
    break;
  case "zero":
    console.log("number is zero.");
    break;
}