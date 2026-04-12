const form = document.getElementById("studentForm");
const studentList = document.getElementById("studentList");

/* Load students on page load */
window.onload = fetchStudents;

/* Add Student */
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const course = document.getElementById("course").value.trim();

  if (!name || !email || !course) {
    alert("All fields are required");
    return;
  }

  const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if (!email.match(emailPattern)) {
    alert("Invalid email format");
    return;
  }

  await fetch("/add-student", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ name, email, course })
  });

  form.reset();
  fetchStudents();
});

/* Fetch Students */
async function fetchStudents() {
  const res = await fetch("/students");
  const data = await res.json();

  studentList.innerHTML = "";

  data.forEach(student => {
    const li = document.createElement("li");
    li.textContent = `${student.name} | ${student.email} | ${student.course}`;
    studentList.appendChild(li);
  });
}