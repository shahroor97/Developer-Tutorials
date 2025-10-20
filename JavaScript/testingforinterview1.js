//Reverse string
const x = 'im a goat';
const m = 'holyyloh'
function reversestring(v) {
    return v.split('').reverse().join('');
}
console.log(reversestring(x));

//Palindrome - check if word is the same backwards
function palindrome(v) {
    return v === v.split('').reverse().join('');
}

console.log(palindrome(x));//false
console.log(palindrome(m));//true

//FizzBuzz - checking for divisibility (% is checking for remainder)
function fazbooz(n) {
    for (i=1 ; i<=n ; i++) {
        console.log(
            i % 3 === 0 && i % 5 == 0 ? 'FizzBizz' :
            i % 3 === 0 ? 'Fizz' :
            i % 5 === 0 ? 'Buzz' :
            i
        )
    }
}

fazbooz(15);

//Factorial

function factorialA(n) {
    let result = 1;
    for (let i=n; i>0; i--) {
        result *= i;
    }
    console.log(result)
}

factorialA(4);

//short factorial version
//factorial is a function taking one argument "n"
const factorialB = n => 
    //ternary condition check if n is 0 or not
    n ? n * factorialB(n-1) : 1;
console.log(factorialB(4))
