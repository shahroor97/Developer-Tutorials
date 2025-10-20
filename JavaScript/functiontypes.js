//regular function
function abra(a,b) {
    console.log(a+b)
}
//arrow function
const sub = (a,b) => {console.log(a-b)};
//anonymous function
const greet = function(name){console.log(name)};






//THIS: arrow functions dont have this, adn they inherti global

const person = {
    name: "Bashar",
    age:"49",
    speak(){console.log(this.name)},
    arrowspeak: () => {console.log(this.name)}
}

person.speak();
person.arrowspeak();