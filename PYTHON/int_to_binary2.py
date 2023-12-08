#!/usr/bin/python3
""" 
    Developer: MAA
    Date: 24/9/2023
    Description: [A program that makes sure the user inputs a positive
    thole number and then runs a function to convert the whole
    number to its binary value this time using RECURSION]
"""

from colorama import Fore


# Handle TypeError and get the right value
while (1):
    try:
        num = int(input(Fore.LIGHTBLUE_EX + "Enter a whole numbers:\t" + Fore.RESET))
        if (num < 0):
            raise ValueError
        break
    except ValueError:
        pass

value = ""
def int_to_bnry(num, value):
    """ A function that converts a whole numbers to its binary value """

    if num <= 0:
        return value

    value = str(num % 2) + value
    num = int(num / 2)
    print(value)

    return str(int_to_bnry(num, value))


print(Fore.GREEN + "The number " + Fore.RESET + f"{num}" + Fore.GREEN + " in binary is " +
      Fore.RESET + f"{int_to_bnry(num, value)}")
