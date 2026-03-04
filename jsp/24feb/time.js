let now = new Date();
let hour = now.getHours(); 

if (hour >= 0 && hour < 12) {
    console.log("Good Morning! ");
} 
else if (hour >= 12 && hour < 17) {
    console.log("Good Afternoon! ");
} 
else if (hour >= 17 && hour < 21) {
    console.log("Good Evening! ");
} 
else if ((hour >= 21 && hour <= 23) || (hour >= 0 && hour < 5)) {
    console.log("Good Night! ");
} 
else {
    console.log("Invalid hour! Please use 0-23.");
}