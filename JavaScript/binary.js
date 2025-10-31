const n = 125;

const binaryn = n.toString(2);
const binarysplit = binaryn.split("0");
const lengths = binarysplit.map(str => str.length); 
const maxi = Math.max(...lengths)

console.log(binaryn)
console.log(binarysplit)
console.log(lengths)
console.log(maxi)

const maxim = Math.max(...n.toString(2).split("0").map(str=>str.length));
console.log(maxim)