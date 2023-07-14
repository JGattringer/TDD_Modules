"""Module that contain the func multiplo"""


def multiplo(var1):
    """Principal function to execute the code"""
    if var1 % 5 == 0 and var1 % 7 == 0:
        return 'FizzBuzz'
    if var1 % 5 == 0:
        return 'Fizz'
    if var1 % 7 == 0:
        return 'Buzz'

    return 'Miss'
