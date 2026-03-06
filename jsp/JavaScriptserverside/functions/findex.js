const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(myFunction);//find the value 
			
function myFunction(value, index, array)//value = 4 index=0  array=4,9, 16,25,29
 {
  return value > 25;
//4>18
}
console.log(first);

