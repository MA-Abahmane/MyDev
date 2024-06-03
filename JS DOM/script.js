
// [setTimeout] 
// set a function to run after a certain amount of time

console.log('Toasting Bread');

const tm = setTimeout(() => {
    // console.log('Bread is ready!');

    clearTimeout(tm); // cancel the setTimeout
}, 5000) // milliseconds



// [setInterval]
// set a function to run repeatedly after a certain amount of time

let c = 0
const nt = setInterval(() => {
    c++
    // console.log(c);

    if (c === 5)
        clearInterval(nt) // cancel the setInterval
}, 999) // milliseconds




/// Regex \\\
/*
 *  \d  Trouver un chiffre
 *  \s  Trouver un caractère d'espacement
 *  \b  Trouver une correspondance au débutou
 *     à la fin d'un mot : \bMOT ou MOT\b
*/

let ex = '[0-9]+ [a-z]+'
let st = 'The Bugatti Veron is a fast car with a top speed of 250 mph'


let srch = st.match(ex) // get speed 
// srch => ['250 mph', index: 52, input: 'The Bugatti...]

let rpl = st.replace(srch[0], '304 mph') // replace speed

console.log(rpl);
console.log("Bugatti Veron Old Speed:", srch[0], '\n\n');


let pos = st.search("Veron");
console.log(pos);  // 12 | if not found returns -1




/// JSON \\\

// JS Dict to JSON
jsonOnj = JSON.stringify({ name: 'John', age: 25, city: 'New York' })

// JSON to JS Dict
jsObj = JSON.parse(jsonOnj)



/// DOM \\\

// Document Object Model
document.title = 'JS DOM'
console.log(document.head);
console.log(document.body);

// Select Elements \\
bx = document.querySelector('#box')   // select by id
lst = document.querySelector('.list')   // select by class (ul)


// Edit Elements \\
bx.style.width = '200px'
bx.style.height = '50px'
bx.style.backgroundColor = 'royalBlue'
bx.style.borderRadius = '10px'

bx.innerHTML = 'To-DO List'
console.log(bx.innerHTML);   // To-DO List

bx.style.fontFamily = 'Roboto'
bx.style.color = 'white'
bx.style.display = 'flex'
bx.style.alignItems = 'center'
bx.style.justifyContent = 'center'


// Create Elements \\

shopList = [
    ['Milk', 2],
    ['Bread', 1],
    ['Eggs', 12],
    ['Butter', 1]
]

i = 1
for (item of shopList) {
    const lstElement = document.createElement('li')

    lstElement.setAttribute('id', i++)  // set an attribute to the element (optional

    lstElement.textContent = `${item[0]}: ${item[1]}`  // the text content of the element

    lst.append(lstElement) //* ADD element<li> to list <ul>

}


let newElm = document.createElement('li')

newElm.textContent = "Apples: 5kg"

newElm.setAttribute('id', 0) // set <li> element id to 0

lst.replaceChild(newElm, lst.firstChild)  //* REPLACE the first element (replaceWith, toReplace)


lst.removeChild(lst.lastChild)  //* REMOVE the last element

// remove the list
// lst.remove()


// add an event listener to the button
let btn = document.querySelector('button').onclick = () => { alert('Button Clicked')} 

let btnAttr = document.querySelector('button').attributes
console.log(btnAttr) // get the second attribute of the button element: class

let btnClass = document.querySelector('button').classList
console.log(btnClass) // get the classes of the button element



console.log(document.body.nodeType) // check is the node contains an element [1] or text [0]
