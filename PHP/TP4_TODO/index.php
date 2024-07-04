<?php
require ('db.php');

$sql = "SELECT * FROM todo";
$stmt = $pdo->query($sql);
$todos = $stmt->fetchAll(PDO::FETCH_ASSOC);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Todo List</title>
    <!-- <link rel="stylesheet" href="styles.css"> -->
    <style>
        body {
            font-family: "Times", sans-serif;
            background: wheat;
        }

        h1 {
            color: wheat;
            text-align: center;
            border: 3px solid rosybrown;
            background: #c5b2b2;
            border-radius: 20px 20px 0 0;
            margin: 10px;
        }

        form {
            text-align: center;
            margin-bottom: 20px;
            color: royalblue;
            border-radius: 0px;
            border: 3px solid rosybrown;
            padding: 20px;
            background: #c5b2b2;
            margin: 10px;
        }

        input {
            width: 150px;
            
        }

        ul {
            list-style-type: none;
            padding: 0;
            display: flex;
            flex-direction: column;
            color: royalblue;
            border: 3px solid rosybrown;
            background: #c5b2b2;
            border-radius: 0 0 20px 20px;
            margin: 10px;
        }

        li {
            margin: 5px;
            padding: 10px;
            border: 1px solid rosybrown;
            display: flex;
            justify-content: space-evenly;
            align-items: center;
            border-radius: 100px;

        }

        a {
            text-decoration: none;
            color: #ff7474; 
        }

        a {
            text-decoration: none;
            color: #47a82f; 
        }

        a.dlt {
            color: #ff7474; 
        }
        
        .undo{
            background: #f8d7da;
            color: #721c24; 
        }

        .done {
            background: #bbf7c9;
            color: #155724;
        }


    </style>
</head>
<body>
    <h1>Todo List</h1>
    <form action="add.php" method="post">
        <input class="input" type="text" name="title" placeholder="New Name..">
        <button class="btn" type="submit">Add</button>
    </form>
    <ul>
        <?php
        if ($todos) {
            foreach ($todos as $todo) {
                $clss = ($todo["done"] ? ' class="done"' : ' class="undo"');
                echo '<li' . $clss . '>
                <br><span id="ind">' . htmlspecialchars($todo["title"]) . '</span>
                        <a href="done-undo.php?id=' . $todo["id"] . '">[Done/Undo]</a>
                        <a class="dlt" href="delete.php?id=' . $todo["id"] . '">[Delete]</a>
                      </li>';
            }
        } 
        else 
        {
            echo "&nbsp; &nbsp; &nbsp; &nbsp;0 résultats";
        }
        ?>
    </ul>
</body>
</html>
