document.addEventListener("DOMContentLoaded", () => {

  const form = document.getElementById("patientForm");

  if (!form) return;

  form.addEventListener("submit", function(e) {

    e.preventDefault();

    const data = {
      name: document.getElementById("name").value,
      age: document.getElementById("age").value,
      email: document.getElementById("email").value
    };

    let patients = JSON.parse(localStorage.getItem("patients")) || [];
    patients.push(data);

    localStorage.setItem("patients", JSON.stringify(patients));

    alert("Saved locally!");
    form.reset();

  });

});