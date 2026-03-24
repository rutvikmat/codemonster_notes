document.addEventListener("DOMContentLoaded", () => {

  const form = document.getElementById("patientForm");

  if (!form) return;

  form.addEventListener("submit", function(e) {

    let age = document.getElementById("age").value;

    if (age <= 0) {
      alert("Age must be greater than 0");
      e.preventDefault();
    }

  });

});