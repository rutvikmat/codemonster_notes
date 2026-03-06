/*console.log("Before Fetch");

fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response => response.json())
    .then(data => console.log(data));

console.log("After Fetch"); */

/*console.log("Start");

setTimeout(function() {
    console.log("Inside Timeout");
}, 2000);

console.log("End");
*/
async function getData() {
    console.log("Before Fetch");

    let response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    let data = await response.json();

    console.log(data);
    console.log("After Fetch");
}

