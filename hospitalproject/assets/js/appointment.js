function validateDate() {
  const selected = document.getElementById("date").value;
  const today = new Date().toISOString().split("T")[0];

  if (selected < today) {
    alert("Cannot select past date");
  } else {
    alert("Appointment booked!");
  }
}