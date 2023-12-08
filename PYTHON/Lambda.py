"""
    Instead of defining the function somewhere and calling it, we can use python's
    lambda functions, which are inline functions defined at the same place we use it.
    So we don't need to declare a function somewhere and revisit the code just for a single time use.

    They don't need to have a name, so they also called anonymous functions. We define a
    lambda function using the keyword lambda.
"""

# Normal function
def add1(a, b):
    return a + b

print(add1(1, 2))


# Lambda function
add2 = lambda a, b : a + b

print(add2(1, 2))


"""
    Exercise
    Write a program using lambda functions to check if a number in the given list
    is odd or even. Print "Odd" if the number is odd or "Even" if not for each element.
"""
l = [2, 4, 7, 3, 14, 19]

for i in l:
    # your code here
    oddOReven = lambda i: print('Even') if i % 2 == 0 else print('Odd')
    oddOReven(i)