#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    length=len(s)
    count, county = 0,0
    d=int(n/length)
    
    #for loop to count occurance of a in s
    for i in s:
        if i == 'a':
            count+=1
            
    # To calculate the resultant count        
    if(n%length == 0):
        return count*d 
    else:
        for j in range(int(n%length)):
            if s[j] == 'a':
                county+=1
        return (count*d)+county
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
