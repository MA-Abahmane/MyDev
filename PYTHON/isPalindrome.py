#!/usr/bin/python3
"""
    Developer: MAA
    Date: 24/9/2023
    Description: [A program containing a method that
    checks if a string is a palindrome or not]
"""

from colorama import Fore as F


s = "MAA|AAM"

def isPalind(s):
    """ checks if a 's' is a palindrome or not and print the answer """

    for i in range(len(s)):
        if (s[i] != s[len(s) - i - 1]):
            return print(F.RED + "Not Palindrome" + F.RESET)

    return print(F.GREEN + "Is Palindrome" + F.RESET)


isPalind(s)
