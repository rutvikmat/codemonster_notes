class car{
    constructor(name,model){
        this.name=name;
        this.model=model;
    }
    display(){
        console.log(this.name,this.model);
    }
}
const car1 = new car("BMW","X5");
car1.display();
const car2 = new car("Audi","A4");
car2.display();