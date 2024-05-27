<?php
/* Date: 2021/05/17
 * Description: PHP file
 * php : Personal Home Page (PHP: Hypertext Preprocessor)
*/
# Single line comment
// Single line comment

// echo : print out \\
print 'Hi PHP! <br>';

"tabulation => \t | End of line => \n 
Carriages return => \r | Vertical tab => \v";

// variables \\
$name = 'Porche 911';
$speed = 320;
$inStock = true;


// constants \\
const PI = 3.14;
echo '<br> <br> PI: ' . PI;


// arrays \\
$colors = array('red', 'green', 'blue');
$colors[] = 'yellow';

// Dictionary \\
$car = array('name' => 'Ferrati', 'speed' => 350, 'inStock' => false); 
$car['colors'] = ['red', 'green', 'blue'];

// foreach ($car as $key => $value)
//      echo '<br>' . $key . ' : ' . $value;


// echo : print out \\
echo "<br> Name    : $name";
echo '<br> Speed   : ' ,  $speed;



// if else \\
echo '<br> Cars : ';

if ($inStock)
echo 'In stock';
# elseif (...)
else
echo 'Out of stock';


// switch case \\
switch ($name){
    case 'Porche 911':
        echo '<br> Price: $100,000';
        break;
    case 'Ferrati':
        echo '<br> Price: $200,000';
        break;
    default:
        echo '<br> Price: $50,000';
}


// match case \\
echo match ($name){
    'Porche 911' => '<br> Price: $100,000',
    'Ferrati' => '<br> Price: $200,000',
    default => '<br> Price: $50,000'
};



//loops \\
echo '<br> Colors  : ';

// $i = 0;
// while ($i < count($colors)){
//     echo '<br>' . $colors[$i];
//     $i++;
// };

foreach ($colors as $color)
     echo '<br>' . $color;

// for ($i = 0; $i < count($colors); $i++){
//     echo '<br>' . $colors[$i];
// };

// do {
//     echo '<br>' . $colors[$i];
//     $i++;
// } while ($i < count($colors));



// functions \\
function carShow($name, $speed, $inStock, $colors)
{
    echo '<br><br> <b> Ladys and Gentlemen, introducing the ' . $name . '!, with a top speed of '
    . $speed . 'km/h. Available in '. count($colors) . ' colors. </b>';
    if ($inStock)
        echo '<br> <i> Currently in stock. Buy now! </i>';
    else
        echo '<br> <i> Soon to be in stock. Order now! </i>';
}

carShow($name, $speed, $inStock, $colors);



// global, static and dynamic variables \\

# Global var: Accessible from anywhere
global $varGlobal;

# Static var: Increase value for each call
function staticFnc() {
    static $varStatic = 0;
    echo '<br> <br> varStatic: ' . $varStatic;
    $varStatic++;
}
#staticFnc(); // 1
#staticFnc(); // 2
#staticFnc(); // 3

# Dynamic var: Variable variables
$varDynamic = 'Hello';

$$varDynamic = 'World'; // $Hello = 'World'

echo '<br> <br> $varDynamic: ' . $varDynamic;
echo '<br> $$varDynamic: ' . $$varDynamic;


// concatenation and assignment operators \\
$s = '<br> Hi ';
$s .= 'There! <br>';
echo $s; # Concat two strings

$n = 5;
$n += 7;
echo $n . '<br>'; # Add 7 to 5



// data types \\
# Boolean
$t = (bool)true;
echo $t . ' ';       # 1
echo var_export($t). '<br>';  # true

$f = (bool)false;
echo (int)$f . ' ';  # 0
echo var_export($f) . '<br>';  # false

$n = (int)'44.5'; # Convert string to int: 44

$a = (float)"12.01"; # Convert string to float: 12.01

$s = (string)12; # Convert int to string: '12'



?>



<?=
// echo : print out
'<br><br> Bye PHP!';
?>
