#!/usr/bin/python3
"""
    Developer: MAA
    Date: 24/9/2023
    Description: [A program containing a method that
    checks if a string is a palindrome or not]
"""

from colorama import Fore as F


max = 20

def FizzBuzz(max):
    """ The FizzBuzz function """
    
    for i in range(max):
        print(f"{i}: ", end='')

        if (i % 3 == 0 and i % 5 == 0):
            print(F.MAGENTA + "FizzBuzz" + F.RESET)
            continue
        if (i % 3 == 0):
            print(F.BLUE + "Fizz" + F.RESET)
            continue
        if (i % 5 == 0):
            print(F.RED + "Buzz" + F.RESET)
            continue
        else:
            print(i)


FizzBuzz(max)
