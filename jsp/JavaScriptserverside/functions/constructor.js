function Circle(radius){
//initialize an object
this.radius=radius;
this.draw=function()
{
    console.log('draw');
}
}
const circle = new Circle(12);
console.log(circle);