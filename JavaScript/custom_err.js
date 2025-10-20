
function isPositive(s) {
    if (s>0) {
        return "YES"
    } else if (s == 0) {
        throw new Error ("Zero Error") 
    } else {
        throw new Error ("Negative Error")
    }
}

try {
    console.log(isPositive(0))
} catch (e) {
    console.log(e.message)
}