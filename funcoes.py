def multiplo(var1):
    if var1 % 5 == 0 and var1 % 7 == 0:
        return 'FizzBuzz'
    elif var1 % 5 == 0:
        return 'Fizz'
    elif var1 % 7 ==0:
        return 'Buzz'
    else:
        return 'Miss'

