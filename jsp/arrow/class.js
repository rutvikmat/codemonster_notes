class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  age() {
    return 2026 - this.year;
  }
}

const myCar = new Car("Tesla", 2022);
console.log(myCar.age()); // 4