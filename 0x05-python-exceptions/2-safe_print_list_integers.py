#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            try:
                print("{:d}".format(item), end=" ")
                count += 1
            except Exception:
                pass
        print()
    except Exception:
        pass
    return count
