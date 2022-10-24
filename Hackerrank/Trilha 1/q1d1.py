#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    dic = {
        "z": 0,
        "p": 0,
        "n": 0
    }
    
    for num in arr:
        if num == 0:
            dic['z'] = dic.get('z') + 1
        elif isP(num):
            dic['p'] = dic.get('p') + 1
        else:
            dic['n'] = dic.get('n') + 1
            
    print(f'{dic.get("p")/len(arr):.6f}')
    print(f'{dic.get("n")/len(arr):.6f}')
    print(f'{dic.get("z")/len(arr):.6f}')

def isP(n):
    return n > 0        
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
