#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_turple = ()
    turple_1 = turple_a + (0, 0)
    turple_2 = turple_b + (0, 0)
    new_turple = turple_1[0] + turple_2[0] + turple_1[1] + turple_2[1]
    return new_turple
