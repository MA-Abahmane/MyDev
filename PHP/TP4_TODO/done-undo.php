<?php

include 'db.php';

$id = $_GET['id'];

$sql = "UPDATE todo SET done = NOT done WHERE id = :id";
$stmt = $pdo->prepare($sql);
$stmt->execute(['id' => $id]);

header('Location: index.php');

?>
