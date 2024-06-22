<?php

// $usrn = $_GET["username"];
// $pswd = $_GET["password"];

$usrn = $_POST["username"];
$usrn = $_POST["password"];

echo "Date : " . date('h:m:s d/m/y') . "<br>";

if (isset($_FILES['files']))
echo "FileName : " . $_FILES['files']['name'] . "<br>";

if (!isset($usrn) || $usrn == ''){
    echo "Error: No Username Provided <br><br>";
    echo '<button><a href="form.html">Return</a></button>';
}
elseif (!isset($pswd) || $pswd == ''){
    echo "Error: No Password Provided <br><br>";
    echo '<button><a href="form.html">Return</a></button>';
}
else {
    echo "Password : $pswd <br>";
    echo "Username : $usrn <br>";
}



// comparison \\




?>