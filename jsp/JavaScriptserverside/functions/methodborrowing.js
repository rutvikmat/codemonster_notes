const person = {
    name: "Pavitra"
};

function greet() {
    console.log(this.name);
}

greet.call(person); // Pavitra