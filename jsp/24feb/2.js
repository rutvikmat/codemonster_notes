var n=1;//initialization
for(;;)
{
    if(n==101)//4==101 
    {
        break;//it takes the control out of for loop
    }
if(n%6==0)
{
    console.log(n);//6,12
    n++;//13
}else
{
n++;//8
}
}//end of the for loop
console.log("end of the for loop");