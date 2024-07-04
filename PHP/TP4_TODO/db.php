<?php

$server = 'mysql:host=localhost;dbname=todolist';
$username = 'root';
$password = '';

try 
{
    $pdo = new PDO($server, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

} 
catch (PDOException $e) 
{
    die('[ERROR] Connection failed: ' . $e->getMessage());
}

