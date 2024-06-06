// JQuery \\
//  $( sélecteur ). action()

$(".hd").hide() // Hide element

$("#lst").css("border", "2px solid black")
$("#lst").css("padding", "10px")
$("#lst").css("width", "150px")
$("#lst").css("height", "150px")

$("h1")
.slideUp(2000)
.slideDown(3000)



console.log(parseInt("0x11"))  // convert STR to INT


// Run after document is ready
$(document).ready(function() {
    
    // check all for a class=last
    $("#lst li").each(function() {
        if ($(this).hasClass("last"))

            $(this).removeAttr("class")
                   .attr("id", "last")
    })  
}) 



// mouse events

$("button").dblclick(function() {
    $("body").hide()
})

$("ul").mouseenter(function() {
    alert("The mouse Entered the list")
})

$("ul").mouseleave(function() {
    alert("The mouse left the list")
})
    





// AJAX \\
let xhttp = new XMLHttpRequest()

// status of the XMLHttpRequest.
console.log("readyState:", xhttp.readyState);
/*
0: request not initialized
1: server connection established
2: request received
3: processing request
4: request finished and response is ready
*/

console.log("status:", xhttp.status);  
//  200: "OK"  /  403: "Forbidden"  /  404: "Page not found"


// when the response is ready
xhttp.onload = function() {
   // Here you can use the Data
   console.log("data:", this.responseText);

}


// Open a request
xhttp.open("GET", "file.json", true)

// Send a request
xhttp.send()

xhttp.abord






// JS Classes \\
class Car {

    constructor(name, speed) 
    {
        this.name = name
        this.speed = speed
    }

    display() 
    {
        console.log("name:", this.name)
        console.log( this.speed)
    }
}

