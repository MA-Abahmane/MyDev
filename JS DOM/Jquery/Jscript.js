

/// JQuery \\\

// JQuery is a library that makes it easier to work with the DOM

/* <script src="Jquery.js"></script> */  // include the library

$("#bx").fadeToggle(3000); // fade in/out

$('button').css('font-style', 'italic'); // change css
$('button, #bx').css('background-color', 'red');  // change css

$('button:first').css('background-color', 'royalblue'); // change css


$('button').click(() => {
    console.log('Button clicked');
    $('button').css('background-color', 'green');
})
