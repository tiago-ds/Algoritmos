#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    aSum = functools.reduce(lambda a, b: a+b, arr)
    print(f'{aSum - max(arr)} {aSum - min(arr)}')
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
