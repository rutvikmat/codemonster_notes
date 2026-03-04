let speed = 45;   // Mbps

if (speed >= 100) {
    console.log("Ultra Fast Internet");
}
else if (speed >= 50) {
    console.log("Fast Internet");
}
else if (speed >= 10) {
    console.log("Average Internet");
}
else {
    console.log("Slow Internet");
}