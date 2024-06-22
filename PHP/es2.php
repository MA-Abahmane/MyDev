<?php
/* Date: 2021/06/22
 * Description: PHP file
 * php : Personal Home Page (PHP: Hypertext Preprocessor)
*/


/* String and Date functions */

$str = 'Ultra me';

echo $str . '<br><br>';

echo 'length: '. strlen($str) . '<br>';

echo 'Uppercased: ' . strtoupper($str) . '<br>';

echo 'Lowercased: ' . strtolower($str) . '<br>';

echo 'Replace space with "-": ' . strtr($str, ' ', '-') . '<br>';


$now =  date('d-m-Y H:m:s') . '<br>';

echo 'Time Now:', $now . '<br>';



// arrays functions \\
$ar = array(2, 5, 1, 3, 4);

echo print_r($ar) . '<br><br>';

array_multisort($ar, SORT_DESC);

echo 'SORT_DESC: ' . '<br>';
print_r($ar);

array_multisort($ar, SORT_ASC);

echo '<br>' . 'SORT_ASC: ' . '<br>';
print_r($ar);

echo '<br><br>';


# merger
$ar2 = array_merge($ar, array(6, 7, 8, 9, 10));


# array_slice : return a portion of an array
array_slice($ar2, 2, 5);  // [1, 2, (3), (4), (5), (6), (7), 8, 9, 10]

# array_splice : remove a portion of an array
array_splice($ar2, 2, 5); // [1, 2, 8, 9, 10]

# array_push : add one or more elements to the end of an array
array_push($ar2, 11, 12, 'End', 99); // [1, 2, 8, 9, 10, 11, 12, 'End', 99]

# array_pop : remove the last element of an array
array_pop($ar2); // [1, 2, 8, 9, 10, 11, 12, 'End']

# array_unshift : add one or more elements to the beginning of an array
array_unshift($ar2, 11, 'Start', 0); // ['Start', 0, 1, 2, 8, 9, 10, 11, 12, 'End']

# array_shift : remove the first element of an array
array_shift($ar2); // [0, 1, 2, 8, 9, 10, 11, 12, 'End']


# print array: print_r($array);
print_r($ar2);

echo '<br><br><br>';


// File manipulation \\
// fopen : open a file

$fileName = 'webdict.txt';

echo 'fileName: ' . $fileName. '<br><br>';

echo 'readFile: ';
readfile("webdict.txt");

// open file: \\
/**
 * r: read only. file must exist
 * r+: read/write. file must exist
 * w: write only. create a new file or truncate an existing file
 * w+: read/write. create a new file or truncate an existing file
 * a: write only. create a new file or write to an existing file
 * a+: read/write. create a new file or write to an existing file
 * x: write only. create a new file. return false if file exists
 * x+: read/write. create a new file. return false if file exists
 */

$f = fopen($fileName, 'r+') or die('Unable to open file!');


// Reading \\

// fread : read from a file
echo '<br>fread: ' . fread($f, filesize($fileName));

// fgets: read a line from a file
// fgetc: read a character from a file
// feof: check if the end of a file has been reached
echo '<br><br>';
while(!feof($f))
    echo fgets($f) . '<br>';


// writing \\

// fwrite : write to a file
 fwrite($f, "\nadd this line");


// close file \\

fclose($f);





?>