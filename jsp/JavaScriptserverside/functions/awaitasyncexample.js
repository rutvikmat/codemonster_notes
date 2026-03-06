const apiUrl="https://api.open-meteo.com/v1/forecast?latitude=12.9752&longitude=77.5439&current_weather=true";
async function myFunction()
{
    console.log('A');
    const response = await fetch(apiUrl);
    console.log(response,'B')
}
myFunction();
console.log('C');