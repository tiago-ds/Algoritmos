#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    c = s[-2:]
    t = int(s[:2])
    ms = s[2:-2]
    if c == 'AM':
        if t == 12:
            return f'00{ms}'
        else:
            return f'{t:02}{ms}'
    else:
        if t == 12:
            return '12' + ms
        else:
            return f'{(t+12):02}{ms}'
        
    if t == 12:
        if c == 'AM':
            return f'00{ms}'
        return '12' + ms
    return f'{((t+12)%12):02}{ms}'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
