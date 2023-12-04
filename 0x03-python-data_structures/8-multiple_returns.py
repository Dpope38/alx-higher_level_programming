#!/usr/bin/python3
def multiple_returns(sentence):
    my_turple = ()
    if len(sentence) == 0:
        my_turple = 0, "None"
    else:
        my_turple = len(sentence), sentence[0]
    return my_turple
