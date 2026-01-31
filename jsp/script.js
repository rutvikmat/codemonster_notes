function showMessage() {
    alert("Hello! This message is from external JavaScript file.");
}

number = parseInt(prompt("Enter a number to find its square:"));
function square(number) {
    alert("The square of " + number + " is " + (number * number));
}
