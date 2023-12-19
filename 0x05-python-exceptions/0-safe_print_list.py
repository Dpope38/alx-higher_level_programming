#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while True:
            print(my_list[count], end=" ")
            count += 1
            if count == x:
                break
    except IndexError:
        pass
    finally:
        print()
    return count
