from sys import stdin

import math


for line in stdin:
    nums = [int(x) for x in line.split()]
    count = nums.pop(0)
    sols = [True for _ in range(count)]
    i = 0
    length = len(nums)
    while i < length:
        j = i+1
        while j < length:
            if not sols[j] and not sols[i] and math.gcd(nums[i], nums[j]) > 1:
                sols[j] = False
                sols[i] = False
            j = j+1
        
        i = i+1
        
    m = max([nums[x] if sols[x] else 0 for x in range(count)])
    print(m)
    

