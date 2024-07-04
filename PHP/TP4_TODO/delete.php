<?php

include 'db.php';

$id = $_GET['id'];

$sql = "DELETE FROM todo WHERE id = :id";
$stmt = $pdo->prepare($sql);
$stmt->execute(['id' => $id]);

header('Location: index.php');

?>
