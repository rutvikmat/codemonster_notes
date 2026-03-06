function add(x,y)
{ 
    return x+y
};

console.log(add(10,20));
//arrow function 
//no need of functionname 
//no need of function keyword 
//just provide the argument and body of function 

const fn = (x,y)=>{
    return x+y;
};

 
console.log(fn(100,200));

const fn1 = (x,y)=>x-y;

r = fn1(2000,1000);
console.log(r);

const fullName = (firstName, lastName) => {
    return firstName+" "+lastName;
};
 console.log(fullName("supriya", "naik"));

 