function createCircle(radius)
{
    return {
        radius,
        draw:function()
        {
            console.log('draw')
        }
    };
}
const circle =createCircle(1);

console.log(circle);
function Circle(radius)
{
    this.radius=radius;
   console.log(this);
    this.draw=function(){
        console.log('draw');
    }
     console.log(this);
}
const Circle1=new Function('radius',`
    this.radius=radius;
    this.draw=function(){
    console.log('drawlll');
    }`);
    const circl=new Circle1(1);
    console.log(circl);
const another = new Circle(1);
console.log(another);