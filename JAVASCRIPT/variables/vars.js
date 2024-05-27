document.write('JS Loaded Successfully!<br><br>')

var a = 1  // global var

let b = a // scope var

const c = a + b // permanent var

let x  // undefined

console.log(x) // print out to console


x, y = a + b + c  // multiple assignment

console.log(y); // y is given (var) by default


function f() {
    var m = 1
}

//console.log(m)
        // Error: function var are declared locals



/* Concatenation */
let s1 = 'Concat'
var s2 = "Me"

s3 = s1 + ' ' + s2  // 'Concat Me'


n = 1 + 7   // 8
n = 1 + '7' // '17'



/* Functions */

/* typeof()
 * return value type */

val = typeof(n) // returns value type
console.log(val)

console.log(typeof(a))  // number

let z
console.log(typeof(z))  // undefined

console.log(typeof(s1))  // string

console.log(typeof(f))  // function

console.log(typeof({}))  // object

console.log(typeof([]))  // object

console.log(typeof(NaN))  // number

console.log(typeof(null))  // object

console.log(typeof(undefined))  // undefined




/* prompt()
 * User Input */
//var name = prompt('What is your name') // get user input 
//document.write(`Welcome ${name}!`);


/* alert()
 * User Output */
//alert(`Welcome Back ${name}`)


/* Number()
 * Convert to Number */
x = Number('01.09')  // 1.09

Number('') // 0

Number(true) // 1

Number(false) // 0

Number('22 11') // NaN

/// + to number converter
y = "5"; // y => string && x => number
x = + y; // + y => number


/* String() | toString()
 * Convert to String */
f = 77

String(f) // '77'

f.toString() // '77'




/* Date */

d = new Date() // current date

console.log('Year :', d.getFullYear());  // Year 2024
console.log('Month :', d.getMonth());  // Month 0 - 11
console.log('Day : ', d.getDate());  // Day in Month 1 - 31
console.log('Week Day : ', d.getDay());  // Week day 0 - 6
console.log('Hour : ', d.getHours());  // Hours 0 - 23
console.log('Minute : ', d.getMinutes());  // Week day 0 - 6
console.log('Seconds : ', d.getSeconds());  // Week day 0 - 6


