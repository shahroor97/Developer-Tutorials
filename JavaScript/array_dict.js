const array = [1,2,3];

array.push(4);
array.push(3); //add to end

console.log(array);

array.pop(); //remove from end
console.log(array);

array.unshift(4); //add to start
console.log(array);
array.shift(); //remove from start
console.log(array);

console.log(array.includes(5)); // checks if it incudes a value

console.log(array.indexOf(4)); // finds index of a value

console.log(array.slice(2,4)); // returns value of index parameter (between index 1,3)

array.splice(2,1); //remove x values from array, start from index w (w,x)

console.log(array);
console.log(array.concat([4,5]));
console.log(array.join("-"));

array.reverse();
console.log(array);

array.sort();
console.log(array);

function iter(n) {
    for (let s of n) {
        console.log(s)
    }
}

//OR

array.forEach(n => console.log(n))

iter(array);

//dictionary

const person = { Name: "Bash", Age: 28};
console.log(`Hi, my name is ${person.Name}, and I am ${person.Age} years old!`);

function keysm(m) {
    for (let x in m) {
        console.log(x, m[x])
    }
}
console.log(Object.keys(person));
console.log(Object.values(person));
keysm(person);

person.city = "Melbourne"; //add a new key
delete person.Age;
keysm(person);
console.log(`${Object.keys(person)} ${Object.values(person)}`)