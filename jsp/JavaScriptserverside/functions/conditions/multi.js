let result = "";


for (let i = 65, j = 97; i <= 90 && j<=122; i++, j++) {
    result += String.fromCharCode(i) + String.fromCharCode(j) + " ";
}

console.log(result.trim());

for(var i =1, j=10; i<=10; i++,j--)
{
    console.log(i*j);//10 18 21
}