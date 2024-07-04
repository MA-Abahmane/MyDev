

l = [2, 4, 55, -6, 7, 8, 9, -512, 1, 124, -13, 514, 15, -6, 317]


let min = l[0]

for (i of l) {
    if (min > i)
        min = i
}

console.log(min);


// *With Reduce
min = l.reduce((min, next) => {
    if (min > next)
        return next 
    else
        return min
})

console.log(min);



// -----------


/*

Le code suivent crée trois valise enfante; <image>, <p> et <script> dans la valise parent <body>, quand le pointeur de la souris survole 
sure l'element <image>, on appelle la fonction "afficher()" qui va change le path de l'image à 'image2.jpg' et l'element <p> va 
contenir le valeur Src de l'image. Si le pointeur sourit s'envole de l'element <image> la fonction "affichée()" vat etre appellee pour changer
l'image a 'image1.jpg' et <p> prendra la valeur src de l'image.

*/


// -------  


function retirer()
{
    x = document.getElementById("s").selectedIndex;
    p = -1;
    el = document.getElementById("t").children;

    for(i = 1; i < el.length; i++)
    {
        if (el[i].children[0].textContent==C[x].titre)
        {
            document.getElementById("t").removeChild(el[i]);
            total=total-C[x].prix;
            document.getElementById("total").innerHTML="<h3>Prix Total : "+
            total+ "</h3>";
        }
    }
}



function ajouter()
{
    i = document.getElementById("s").selectedIndex;
    l = document.createElement("tr");
    d = document.createElement("td");

    d.textContent=C[i].titre;
    document.getElementById("t").appendChild(l);
    l.appendChild(d);

    dd = document.createElement("td");
    dd.textContent=C[i].prix;

    l.appendChild(dd);
    total=total+C[i].prix;

    document.getElementById("total").innerHTML="<h3>Prix Total : "+
    total+ "</h3>";
}



function afficher()
{
    i = document.getElementById("s").selectedIndex;
    document.getElementById("lblisbn").innerHTML="<h2>Livre "+ C[i].ISBN +"</h2>"
    document.getElementById("lbltitre").innerHTML= C[i].titre ;
    document.getElementById("lblprix").innerHTML= C[i].prix;
    document.getElementById("image").src=C[i].image;
}



C = [
{"ISBN":"01234","titre":"Langage C","image":"langagec.jpg","prix":150},
{"ISBN":"56789","titre":"Programmation Javascript","image":"javascript.jpg","prix":250},
{"ISBN":"11778","titre":"Laravel","image":"laravel.jpg","prix": 200}
]

var total = 0;
function charger()
{
    liste = document.getElementById("s");

    for (elt of C)
    {
        x = document.createElement("option");
        x.value= elt.ISBN;
        x.textContent= elt.titre;
        liste.appendChild(x);
    }
}

charger();
