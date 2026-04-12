function sum(...numbers){
    return numbers.reduce((A,B)=>A+B,0);
}
console.log(sum(1,2,3,4));
