# Author: Gubanyi
# Title: Traveling on the Axis
# Date: 9/19/2023

# URL = https://contest.ucup.ac/contest/1339/problem/7109

import sys
sys.setrecursionlimit(100100)

def memoize(f):
    memos = {}
    def wrapper(p,q,use_input_lights):
        if (p,q,use_input_lights) not in memos:            
            memos[(p,q,use_input_lights)] = f(p,q,use_input_lights)
        return memos[(p,q,use_input_lights)]
    return wrapper
    
@memoize
def t(p, q, use_input_lights):
    if p >= q:
        return 0

    if ((use_input_lights and input_lights[p] == "1") or
        (not use_input_lights and toggled_lights[p] == "1")):

        return 1 + t(p+1, q, not use_input_lights)
    else:
        return 1 + t(p, q, not use_input_lights)


input_lights = input()
toggled_lights = "".join(["1" if c == "0" else "0" for c in input_lights])
total = 0

for p in range(0, len(input_lights)):
    for q in range(p+1, len(input_lights)+1):
        total += t(p, q, True)
print(total)
