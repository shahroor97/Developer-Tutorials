function hello_world() {
    return console.log("Hello World!")
};

function numandstr(){
     const i = 0;
     const n = 1.1;
     const x = "3";
     const l = "3.0";

     console.log(i+parseInt(x)); //3
     console.log(i+n); //1
     console.log(i+parseInt(l)); //3
     console.log(i+parseInt(n)); //1
     console.log(n+parseInt(x)); //4
     console.log(n+parseFloat(l)); //4
     console.log(n+Number(x))
     console.log(l+x)
};

function rect(a,b) {
    return {
        perimeter: () => a*2+b*2,
        area: () => a*b
    }
}
function factorial(n) {
    result = 1;
    for (let i = 1; i<=n; i++){
        result *= i;
    }
    return result
}

function function5(){

}

function function6(){

}


hello_world();

numandstr();

const x = rect(3,4)
console.log(x.perimeter());
console.log(x.area());
console.log(factorial(4));