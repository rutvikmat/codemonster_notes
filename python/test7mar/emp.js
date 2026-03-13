const employee = {
  name: "RUTVIK",
  id: 1,
  role: "devloper",
  isRemote: true,
   display(){
    console.log(`${this.name} is currently online.`);
  }
};

console.log(employee.role);
console.log(employee.name);
employee.display();