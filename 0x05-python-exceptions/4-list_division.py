#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                if i >= len(my_list_1) or i >= len(my_list_2):
                    raise IndexError
                val1 = my_list_1[i]
                val2 = my_list_2[i]
                instance1 = isinstance(val1, (int, float))
                instance2 = isinstance(val2, (int, float))
                if not instance1 or not instance2:
                    raise TypeError
                if val2 == 0:
                    raise ZeroDivisionError
                result.append(val1 / val2)
            except IndexError:
                print("out of range")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
    finally:
        return result
