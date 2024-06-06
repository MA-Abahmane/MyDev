
// [setTimeout] 
// set a function to run after a certain amount of time

console.log('Toasting Bread');

const tm = setTimeout(() => {
    // console.log('Bread is ready!');

    clearTimeout(tm); // cancel the setTimeout
}, 5000) // milliseconds


clearTimeout(tm)


// [setInterval]
// set a function to run repeatedly after a certain amount of time

let c = 0
const nt = setInterval(() => {
    c++
    // console.log(c);

    if (c === 5)
        clearInterval(nt) // cancel the setInterval
}, 999) // milliseconds


clearInterval(nt)


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
    ['Milk', '3L'],
    ['Bread', 7],
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


newElm.setAttribute('id', 0) // set <li> element id to 0;


lst.replaceChild(newElm, lst.firstChild)  //* REPLACE the first element (replaceWith, toReplace)


lst.removeChild(lst.lastChild)  //* REMOVE CHILD the last element

// REMOVE ELEMENT remove the list
      lst.remove()


// Select All \\
LIs = document.querySelectorAll('li') // .length

for (LI of LIs)
    LI.style.border = '1px solid black'



// add an event listener to the button
let btn = document.querySelector('button').onclick = () => { 
    alert('Clear List?')
    // remove all list contents
    while (lst.firstChild) {
        lst.removeChild(lst.firstChild)
    }
    // remove the list
    //  lst.remove()
} 

let btnAttr = document.querySelector('button').attributes
console.log(btnAttr[1]) // get the second attribute of the button element: class

let btnClass = document.querySelector('button').classList
console.log('Classes :', btnClass.value) // get the classes of the button element



// Node Types \\
console.log(document.head.nodeType) // check is the node contains an element [1] or text [0]



/*
<ul id='list'>
    <li> One </li>
    <li> Two </li>
    <li> Three </li>
</ul>

*/

ul = document.querySelector('#list2')
li = document.querySelectorAll('li')[1] // get the second <li> element


li.parentNode       // (ul)  get the Parent of the <li> element


// with text
ul.firstChild        // get the First Child of the <ul> element

ul.lastChild          // get the Last Child of the <ul> element

ul.childNodes         // get all Children of the <ul> element

// with text
li.nextSibling            // get the Next Sibling of the <li> element

li.previousSibling


// no text/ element only
ul.firstElementChild      // get the First Element Child of the <ul> element

ul.lastElementChild       // get the Last Element Child of the <ul> element

ul.children               // get all Children Elements of the <ul> element

// no text/ element only
li.nextElementSibling     // get the Next Element Sibling of the <li> element

li.previousElementSibling



// Classes \\
console.log(ul.classList)   // get the classes of the <ul> element

ul.classList.add('added!')    // add a class to the <ul> element



ul.removeAttribute("class")   //  remove attribute class from the <ul> element




// Event Listeners \\

// add a button to the document
btn = document.createElement('button')

btn.textContent = 'Clear Documenr'

btn.setAttribute('class', 'btnR')

btn.style.border = '3px double gray'
btn.style.borderRadius = '20px'

document.body.append(btn)



/// Add Event Listener \\\

// btn on click
btn.addEventListener('click', () => {
    
    let ansr = confirm('Do you want to Clear the Document?')

    if (ansr == true){
        while (document.body.firstChild)
            document.body.removeChild(document.body.firstChild)
    }
})

btn.addEventListener('dblclick', () => {

    if (ansr == true){
        while (document.body.firstChild)
            document.body.removeChild(document.body.firstChild)
    }
})


btn.addEventListener('mouseover',  ovr = () => {  // MOUSE OVER element
    btn.style.background = 'red'
})

btn.addEventListener('mouseout', out = () => {  // MOUSE OUT of element
    btn.style.background = 'crimson'
})


// Remove Event Listeners

setTimeout(() =>{
    btn.removeEventListener('mouseover', ovr)
    
    btn.removeEventListener('mouseout', out)

    btn.style.background = 'white'
}, 4000)




/// Mouse Events \\\

//  HOVER: mouseover,  mouseout

//    CLICK: mousedown,  mouseup

//      CLICKED:  click, dblclick

// MOUSEMOVE
document.body.addEventListener('mousemove', (e) => {
    console.log(`Screen X/Y: ${e.screenX} ${e.screenY} | Client X/Y ${e.clientX} ${e.clientY}`);
})




/// Keyboard Events \\\

// keyup: all keys  |  keydown: all keys  |  keypress: letter keys

document.body.addEventListener('keypress', (key) => {
    if (key['key'] == 'Delete')   // [KeyCode] 
        alert('Key [Delete] pressed')

    console.log(key);
})