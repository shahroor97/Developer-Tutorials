const s = 'asbcedjhaelcasiucheoad';

//For and if
function vowelsAndConsonants(s) {
    const vowels = 'aeiou'
    for (let i of s)  {
        if (vowels.includes(i)) console.log(i)
    }
    for (let i of s) {
        if (!vowels.includes(i)) console.log(i)
    }
}

vowelsAndConsonants(s)



//While

function deleteeverything(f) {
    while (f !== "") {
        f = f.slice(0,-1);
        console.log(f)
    }
}

deleteeverything(s);


//Conditionals

//Ternary Operator "?" - Quick one line if/else
const x = 8;
const size = x > 10 ? 'big' : x === 10 ? 'equal' : 'small'; //“If x > 10 → big, else if x === 10 → equal, else → small”
console.log(size);

//Nullish Coalescing - User as a backup default for null values or undefined
const userInput = null;
const name = userInput ?? 'Guest';
console.log(name); //Guest

const score = 0;
const results = score ?? 100;
console.log(results); //0

//Optional Chaining (Think of ?. as a safety guard: “Only go deeper if the thing before it exists.”)
const user = { profile: {age: 30}};
const ghost = null;
console.log(ghost?.profile?.age); // Doesnt crash but gives undefined value
//console.log(ghost.age); <---this would crash

//Truthy /Falsy -- JS treats certain values as false automatically false, 0, '', null, undefined, NaN

'hello' ? console.log('truth') : console.log('false');
0 ? console.log('truth') : console.log('false');
if (undefined) console.log('truth'); //doesnt run

//Logical operators &&, ||, ! and short circuits

const z = 5, y = 10;
if (z < 10 && y >5) console.log('both are true');
if (z === 5 || y === 0) console.log('one is true');
if (!(z>5)) console.log('x is not greated than 5');
//shortcircuits below
z > 3 && console.log('runs only of true');
z < 3 || console.log('runs only if false');