#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    numpairs=0
    multis = []#will be used in outside for loop. If the value is already in multis, will skip
    for x in range(n):
        if(ar[x] in multis):#checking to see if element in position x also occurred earlier, in which case it was already counted so would need to skip over it
            print("This is working")
            continue
        counter=1
        for a in range(x+1,n):
            if(ar[a]==ar[x]):
                counter+=1
                multis.append(ar[x])
                if(counter%2==0):
                    numpairs+=1
    return numpairs

def checker(ar, a):
    for x in range(a):
        if(ar[x]==ar[a]):
            return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
