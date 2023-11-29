#!/usr/bin/python
def fizzbuzz():
    for i in range(0, 101):
        if i % 3 == 0 and 1 % 5 != 0:
            print("Fizz ", end='')
        elif i % 5 == 0 and i % 3 != 5:
            print("Buzz ", end='')
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz ", end='')
        else:
            print("{}".format(i), end='')

