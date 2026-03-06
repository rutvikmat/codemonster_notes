//let a;
try{
console.log(a);//it prints the simple values but not the dom objects
}catch(error)
{
   // console.log(error);
   console.dir(error);//it prints the dom objects in the browser
}
console.log(3+4);
let person=
{
name: "Pavitra",
age:21
}
console.dir(person);
