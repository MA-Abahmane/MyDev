<?php
require('User.php');

$u1 = new User('Ali', 44, 'Ali@umamiya.com');

echo $u1->getInfo();
echo "<br>";

$u1->setName('Ali Alj');
echo "<br>";

echo 'Name Edited: ' . $u1->getName();
echo "<br>";


$a1 = new Admin('Alex', 12, 'alexx@umamiya.com');

echo $a1->message();


echo User::me(); # static method

echo User::$role; # static property



// Class | Object functions \\ 

is_a($u1, 'User'); # true

get_class($a1);    # Admin

get_parent_class($a1); # User

get_declared_classes(); # ['User', 'Admin']

get_class_vars('Admin'); # ['name', 'email']

get_class_methods($a1); # ['message', 'getInfo', 'getName', 'setName']




?>