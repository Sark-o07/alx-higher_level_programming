#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    if len_sen == 0:
        return 0, None
    else:
        first_char = sentence[0]
        return len_sen, first_char
