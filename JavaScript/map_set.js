//Set up a map

const map = new Map();

//Update and manipulate values in map
map.set('a',1); //add key value pair
map.set('b',2);
console.log(map.get('a')); //get a value for a key
map.delete(2); //delete
console.log(map.has(0)); //confirm if it contains a value
console.log(map.size);

for (let [k,v] of map) console.log(k,v);



//Set up a set

const set = new Set([2,5,3,1]);
set.add(55); //add values
console.log(set);
set.delete(1); //delete a value
console.log(set);
set.forEach(n => console.log(n));


//Map functions from string to get phone number as a phone book
const phonebookdetails = "3\nsam 12345678\njack 18273645\nmike 12345678\nsam\nluke\nmike"
function phonebook(input) {
    const map = new Map();
    const lines = input.split("\n");
    const n = parseInt(lines[0], 10);

    for (let i=1 ; i<=n ; i++) {
        const [name, number] = lines[i].trim().split(" ");
        map.set(name, number)
    }

    for (let i=n+1 ; i<lines.length ; i++) {
        const q = lines[i].trim();
        if (map.has(q)) {
            console.log(`${q}=${map.get(q)}`)
        } else {
            console.log("Not Found")
        }
    }   
}

phonebook(phonebookdetails);