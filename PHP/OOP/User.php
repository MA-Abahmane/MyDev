<?php

//  namespace OOP;

abstract class User
{

    // properties
    protected $name;    // accessible in the class and its children 
    private $age;       // accessible only in the class
    public $email;      // accessible everywhere

    public static $role = 'User'; // static property


    // toString
    public function __toString() {
        return $this->getInfo();
    }

    // constructor
    public function __construct($name, $age, $email) {
        $this->name = $name;
        $this->age = $age;
        $this->email = $email;
    }

    public static function me() {
        return "I am a User";
    }

    // methods
    public function getInfo() {
        return ($this->name . " is " . $this->age . " years old and his email is " . $this->email);
    }

    // Getter/Setter
    public function getName() {
        return $this->name;
    }

    public function setName($name) {
        $this->name = $name;
    }

    // Abstract Method: Must be defined in the child class
    abstract public function message();

    // __clone: is called when an object is cloned
    public function __clone() {
        echo "<br>-User " . $this->name . " is Cloned-<br>";
    }

    // __call: is called when an undefined method is called
    public function __call($name, $args) {
        echo "Method " . $name . " does not exist in the class";
    }

    // Destructor
    function __destruct() {
        echo "<br>-User " . $this->name . " is Cleared-<br>";
    }

}



class Admin extends User
{

    // abstract method implementation
function message() {
    return $this->name . " is an Admin";
}

}




?>