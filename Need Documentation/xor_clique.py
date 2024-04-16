# Author: Gubanyi
# Title: Live Love
# Date: 9/18/2023

# URL = https://contest.ucup.ac/contest/1339/problem/7112

T = int(input())

for test in range(T):
    n = int(input())
    line = input()
    nums = [int(num) for num in line.split()]

    result = 0

    for p in range(0, 31):
        count = 0
        i = 0
        while i < len(nums):
            if 2**p > nums[i]:
                count += 1
                nums.pop(i)
            else:
                i += 1
        if count > result:
            result = count

    print(result)
        
        

