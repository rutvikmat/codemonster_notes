
    const form = document.getElementById("myForm");
    form.addEventListener("submit", function(event) {
        event.preventDefault(); 
        const username = document.getElementById("username").value;
        const mobile = document.getElementById("mobile").value;
        alert("Username: " + username + "\nMobile No: " + mobile + "\nForm submitted successfully!");
    });
