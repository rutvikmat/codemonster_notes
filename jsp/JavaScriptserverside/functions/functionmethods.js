function Circle(radius)
{
    this.radius=radius;
    this.draw=function(){
        console.log('avani');
    }
}
Circle.call(Circle,1);
//console.log(Circle.apply({},[1,2,3]));