for(var n=1;n<201;n++)//23 11 21
{
    if(n%10==0)//10%10 0==0 20%10 0==0
    {
        continue;//goes to n++ or next iteration
    }else{
      console.log(n);//12345678911 12 13 14 15 16 17 18 19 
    }
}