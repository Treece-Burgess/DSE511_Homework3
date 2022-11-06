#!/usr/bin/env python3


def is_palindrome(num=None):
    pal = ''
    for i in range(len(str(num))-1,-1,-1):
        pal += str(num)[i]
    if(int(pal) == num):
        return True
    else:
        return False
