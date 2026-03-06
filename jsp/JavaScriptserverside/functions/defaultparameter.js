function myFunction(x, y=10) {
//x  is 10 if not passed or undefined
  return x + y;
}
function myFunction1(x, y=20) {
//x  is 10 if not passed or undefined
console.log(x);
console.log(y);
  return x + y;
}
console.log(myFunction1(10));
console.log(myFunction1(100,200));

/*function sum(x,y,z)
{
    console.log("three para");
    return x+y+z;
}*/
function sum(...values)//rest parameter converts into array
{   var sum=0
     for(let v of values)//enhanced for loop 
     {
        sum+=v;
     }
     console.log(sum);
}
sum(10,20,30);
sum(10,20,30,67,89,90,12,34);
//console.log(s);