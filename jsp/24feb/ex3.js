let number = 5;

if (number > 0) {
    console.log("The number is positive.");
    
    if (number % 2 === 0) {
        console.log("It is also even.");
    } else {
        console.log("It is also odd.");
    }

} else if (number < 0) {
    console.log("The number is negative.");
} else {
    console.log("The number is zero.");
}