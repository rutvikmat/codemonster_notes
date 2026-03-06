function Circle(radius)
{
    this.radius=radius;
    //private properties
    let defaultLocation = {x:0,y:0};

    //getter method
    this.getDefaultLocation=function()
    {
        return defaultLocation;
    }
    //private methods
    let computeOptimumLocation = function(factor)
    {
        console.log(defaultLocation);
        console.log("private methods"+factor);
    }
    this.draw = function()
    {
        computeOptimumLocation(0.1);
        console.log('draw');
    };
    Object.defineProperty(this,'defaultLocation',{
    get: function()
    {
        return defaultLocation;
    },
    set:function(value)
    {
        if(!value.x || !value.y)
            throw new Error('Invalid Location');
            defaultLocation=value;
        
    }
});
}
const circle = new Circle(10);
circle.defaultLocation=1;
circle.defaultLocation = false;//here it creates a new property called defaultLocation
//it is not accessing the private method which is inside the function
console.log(circle);
circle.defaultLocation=true;
console.log(circle.defaultLocation);
circle.draw();//inside this defaultLocation property value are x=0,y=0
//circle.computeOptimumLocation(90.0);
circle.getDefaultLocation();
console.log(circle);
