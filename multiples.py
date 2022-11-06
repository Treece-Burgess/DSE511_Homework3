#!/usr/bin/env python3


for val in range(1,101):
    if(val%3==0 and val%5==0):
        print('AB')
    elif(val%3==0):
        print('A')
    elif(val%5==0):
        print('B')
    else:
        print(val) 
