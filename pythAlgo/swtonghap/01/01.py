#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'balancedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSum(arr):
    N = len(arr)

    sum1toN, sumNto1 = [0 for _ in range(N)], [0 for _ in range(N)]
    sum1toN[0] = arr[0]
    sumNto1[N-1] = arr[-1]

    for i in range(1, N):
        sum1toN[i] = sum1toN[i-1] + arr[i]
        sumNto1[N-i-1] = sumNto1[N-i] + arr[N-1-i]

        if sum1toN[i] == sumNto1[i]:
            return i


print(balancedSum([1, 2, 1]))