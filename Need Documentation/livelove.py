# Author: Gubanyi
# Title: Live Love
# Date: 9/18/2023

# URL = https://contest.ucup.ac/contest/1339/problem/7102

import math

T = int(input())

for i in range(T):
    line = input()
    items = line.split()
    n = int(items[0])
    m = int(items[1])

    smax = m
    if m > 0:
        perfects = m
        non_perfects = n-m

        x = perfects / (non_perfects + 1)
        smin = math.ceil(x)
        
    else:
        smin = 0

    print(smax, smin)
