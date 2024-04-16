

from sys import stdin
import math

for line in stdin:
    m = 0
    nums = []
    inputs = line.split()
    inputs.pop(0)
    for x in inputs:
        ix = int(x)
        nums.append(ix)
        if ix > m:
            m = ix
        
    i = 2
    max_factor = math.sqrt(m)

    while i < max_factor:
        j = 0
        c = 0
        while j < len(nums):
            if nums[j] % i == 0:
                c = c + 1
            if c == 2:
                break
            j = j+1
        if c == 2:
            j = 0
            while j < len(nums):
                if nums[j] % i == 0:
                    del nums[j]
                else:
                    j = j+1

        i = i + 1
    m = max(nums)
            

    print(m)
    
