

l = [2, 4, 55, -6, 7, 8, 9, -512, 1, 124, -13, 514, 15, -6, 317]


let min = l[0]

for (i of l) {
    if (min > i)
        min = i
}

console.log(min);

var array = [36, 25, 6, 15];

array.reduce(function(accumulator, currentValue) {
  return accumulator + currentValue;
}, 0); // 36 + 25 + 6 + 15 = 82

// -----------


/*

Le code suivent crée trois valise enfante; <image>, <p> et <script> dans la valise parent <body>, quand le pointeur de la souris survole 
sure l'element <image>, on appelle la fonction "afficher()" qui va change le path de l'image à 'image2.jpg' et l'element <p> va 
contenir le valeur Src de l'image. Si le pointeur sourit s'envole de l'element <image> la fonction "affichée()" vat etre appellee pour changer
l'image a 'image1.jpg' et <p> prendra la valeur src de l'image.

*/


// -------  


lst = [
    {"ISBN":"01234", "titre":"Langage C", "image":"langagec.jpg", "prix":150},
    {"ISBN":"56789", "titre":"Programmation Javascript", "image":"javascript.jpg", "prix":250},
    {"ISBN":"11778", "titre":"Laravel", "image":"laravel.jpg", "prix":200}
]

// Create List
ul = document.createElement('ul')

document.body.append(ul)
document.body.style.color = 'white'


// Load up list
var i = 0
function charger(ul, books) {
    
    for (book of books) {
        li = document.createElement('li')

        id = document.createElement('p')
        h2 = document.createElement('h2')
        img = document.createElement('img')
        prix = document.createElement('p')

        h2.textContent = book["titre"]

        li.setAttribute('id', `l${i}`)
        li.setAttribute('onclick', `afficher(l${i++})`)
        li.append(h2, id, img, prix)

        ul.append(li)
    }
} 


var active = false
function afficher(id) {
    li = id

    if (!active)
    {    li.children[1].textContent = book["ISBN"]
        li.children[2].setAttribute('src', book["image"])
        li.children[3].textContent = book["prix"]
        active = true
    }
    else {
        li.children[1].textContent = ''
        li.children[2].removeAttribute('src')
        li.children[3].textContent = ''
        active = false
    }
}


// add a book
function ajouter(book) {
    ul = document.querySelector('ul')

    lst.push(book)
    l = [book]

    charger(ul, l)
}


function retirer(book) {
    ul = document.querySelector('ul')


}


charger(ul, lst)
ajouter({"ISBN":"00001", "titre":"B", "image":"VB1.jpg", "prix":140})
ajouter({"ISBN":"00341", "titre":"C#", "image":"VC1.jpg", "prix":120})
