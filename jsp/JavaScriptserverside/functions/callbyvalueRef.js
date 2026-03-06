let x={value:10};
let y=x;
x.value=20;
console.log(x.value);
console.log(y.value);
//another example
let number =10;
function increase(number)
{
    number++;
    console.log(number);
}
increase(number);
console.log(number);
// call by ref example
let obj = {value:10};

function increase(obj)
{
    obj.value++;
}
increase(obj);
console.log(obj);