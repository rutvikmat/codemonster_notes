//fetch('http://example-api.com')  makes the request to an api the function returns a promise
//which is fulled with response object.

// fetch('http://example-api.com')
// .then(response=>
// {
// console.log(response);
// }
// ).catch(response=>
// {
// console.log("error");
// }
// )
let isLoading=true;
const apiUrl="https://api.open-meteo.com/v1/forecast?latitude=12.9752&longitude=77.5439&current_weather=true";
fetch(apiUrl).then(response=>{
    if(!response.ok)
    {
        throw new Error('error:'+response.status)
    }
    return response.json();
})
.then(data=>{
    console.log('Temparature', data.current_weather.temperature)
})
.catch(error=>
{
console.error('error in catch ',error)
}
)
.finally(()=>{
isLoading=false;
})
/*
myPromise runs in the following sequences
.then(()=>{})
.catch(()={})
.finally(()=>{})
    */