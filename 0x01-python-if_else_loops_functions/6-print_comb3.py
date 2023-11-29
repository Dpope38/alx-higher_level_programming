#!/usr/bin/python3
for firstNumber in range(0, 10):
    for secondNumber in range(firstNumber + 1, 10):
        if firstNumber == 8 and secondNumber == 9:
            print("{}{}".format(firstNumber, secondNumber))
        else:
            print("{}{}, ".format(firstNumber, secondNumber), end='')

