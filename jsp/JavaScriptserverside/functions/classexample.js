class Car {
    //constructor is special function it is used to assign the value
    //to the object when  object is created.
  constructor(carId,name, year) {
    this.carId=carId;
    this.name = name;
    this.year = year;
  }
}

const carObj = new Car(1000,"Hondai",2000);//constructor is called 

console.log(carObj);

const carObj1 = new Car(2000,"BMW",1995);//constructor is called 
console.log(carObj1);