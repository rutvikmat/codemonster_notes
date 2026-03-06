    const circle ={
        radius:1,
        length:100,
        width:200,
        draw(){
            console.log('draw');
        }
    };
    // const another = {};
    // for(let key in circle)
    // {
    //     another[key]=circle[key];
    // }

    // console.log(another);

    //another way of cloning the object 
    // const another =Object.assign({
    //     color:'Yellow',
    //     type:'semicircle',
    // },circle);
    // console.log(another);
//another way of cloning object
const another = {...circle};
console.log(another);
