const form = document.querySelector("#userForm");
form.addEventListener("submit", (event) => {
  event.preventDefault(); // Stops the page reload
  console.log("Form data ready to be sent!");
});