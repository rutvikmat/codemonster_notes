const prom= new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve(" promise resolved");
    },3000);
}
);
prom.then(res => console.log(res));
