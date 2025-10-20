function regexVar() {
  let re = /^([aeiou]).*\1$/; // starts and ends with same vowel
  return re;
}
const s = 'abcdcda';
// Get the regex
let re = regexVar();
// Test it
console.log(re.test(s)); // true or false
// Or match
console.log(s.match(re)); // returns match details or null