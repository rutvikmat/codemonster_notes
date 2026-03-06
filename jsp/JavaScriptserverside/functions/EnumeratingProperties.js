function Circle(radius)
{
    this.radius=radius;
    this.PI=3.142;
    this.draw=function()
    {
        console.log('draw');
    }
}
const circle= new Circle(10);
for(let key in circle)
{
    console.log(key);
}

for(let key in circle)
{
    if(typeof circle[key]!=='function')
    {
        console.log(key, circle[key])
    }
}
const keys=Object.keys(circle);
console.log("lkslkdjsd"+keys);

if('radius' in circle)
{
    console.log('Circle has a radius');
}