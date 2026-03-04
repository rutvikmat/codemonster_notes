const search = document.querySelector("#searchBox");
search.addEventListener("input", (e) => {
  console.log("Searching for:", e.target.value);
});