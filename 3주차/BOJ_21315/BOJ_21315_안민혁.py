
import math
import sys
from collections import deque
from itertools import product
input = sys.stdin.readline

# 완탐 + 구현

N = int(input())
final = list(map(int, input().split()))
start = list(range(1,N+1))
k_list = range(1, math.ceil(math.log(N,2)))

for cand in list(product(k_list, k_list)):
    stack = start[:]
    for k in cand:
        for i in range(1, k+2):
            if i==1:
                num = 2**k
                stack = stack[-num:] + stack[:-num] 
            else:
                num = 2**(k-i+1)
                stack = stack[prev-num:prev] + stack[:prev-num] +stack[prev:]
            prev = num

    if final == stack:
        sys.stdout.write(' '.join(map(str, cand)))
        break