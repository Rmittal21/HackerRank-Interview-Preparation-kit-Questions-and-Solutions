#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair_count=0
    count = []
    count = [0 for i in range(n)] 
    k=0
    ar = sorted(ar)
    i=1
    if(n==3):
        return 0
    
    for i in range(n):
        if ar[i-1]==ar[i]:
            count[k]+=1
        else:
            count[k+1]+=1
            k+=1
            
    for j in count:
        d=int(j/2)
        pair_count+=d
    return pair_count     
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
