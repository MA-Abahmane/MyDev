#!/usr/bin/python3

def roman_to_int(roman_string):

    if (roman_string is None or type(roman_string) != str):
        return (0)

    Rnum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_n = 0
    n = 0

    for c in roman_string:
        
        Cval = Rnum[c]

        if (prev_n < Cval):
            n -= (2 * prev_n)

        n += Cval
        prev_n = Cval

    return (n)




roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

