#!/usr/bin/python3
"""
    Developer: MAA
    Date: 24/9/2023
    Description: [This module contains a program that works like
    a basic calculator using Object Oriented Programming]
"""

from colorama import Fore as F


class Calc:
    """ The Calc Class """

    def __str__(self):
        """ Class string """
        return str(F.GREEN + "\nAnswer:" + F.RESET)


    def __init__(self, a=0, b=0, sin=2):
        """ Constructor """
        
        self.a = a
        self.b = b
        self.sin = sin


    def calculator(self):
        """ main calculator processor """
        try:
            if (self.sin == 1): 
                return self.add()
            elif (self.sin == 2):
                return self.sub()
            elif (self.sin == 3):
                return self.mul()
            elif (self.sin == 4):
                return self.div()
            elif (self.sin == 5):
                return self.mod()
            elif (self.sin == 6):
                return self.sqr()
            else:
                return
        except Exception as err:
            print(F.RED + str(err) + F.RESET)


    def add(self):
        """ addition """
        print(f"{self.a} + {self.b} = {self.a + self.b}")
        return self.a + self.b


    def sub(self):
        """ subtraction """
        print(f"{self.a} - {self.b} = {self.a - self.b}")
        return self.a - self.b


    def mul(self):
        """ multiplication """
        print(f"{self.a} x {self.b} = {self.a * self.b}")
        return self.a * self.b


    def div(self):
        """ division """
        print(f"{self.a} / {self.b} = {self.a / self.b}")
        return self.a / self.b


    def mod(self):
        """ modulo """
        print(f"{self.a} mod {self.b} = {self.a % self.b}")
        return self.a % self.b


    def sqr(self):
        """ square """
        print(f"{self.a} {self.b} = {self.a ** self.b}")
        return self.a ** self.b


# Get correct value from user and run the calcul class
while(1):
    try:
        print(F.GREEN + "\n_-_-_-_-_-_-_-_-_-_- Calcular -_-_-_-_-_-_-_-_-_-_\n" + F.RESET)
        num1 = int(input("Enter your first Number \n"))
        num2 = int(input("Enter your second Number\n"))
        sin = int(input("Enter the number of operation: \n1:addition 2:subtraction 3:multiplication 4:division 5:modulo 6:square\n"))

        if (sin not in range(1, 7)):
            raise ValueError
    except ValueError:
        print(F.RED + "INPUT ERROR, try again" + F.RESET)
        pass
    else:
        s = Calc(num1, num2, sin)
        print(s)
        print(s.calculator())
