const testPromise = new Promise((resolve, reject)=>
{
    const result = 10+5;
    if(result===15)
    {
        resolve("fulfilled");
    }else{
        reject({message:'something went wrong'});
    }
});
testPromise.then(message => {
    console.log(message);
}).catch(message=>
{
    console.log(message);
}
)