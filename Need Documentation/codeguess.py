(p, q) = (int(x) for x in input().split())

line = input()

possible_nums = list(range(1, 10))
possible_nums.remove(p)
possible_nums.remove(q)

if line == "AABB":
    # Remove all numbers less than q
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] < q:
            del possible_nums[i]
        else:
            i += 1

elif line == "ABAB":
    # Remove all less than p
    if p + 1 == q:
        possible_nums = []
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] < p:
            del possible_nums[i]
        else:
            i += 1
            
            
elif line == "ABBA":
    # Remove all less than p, and greater than q
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] < p:
            del possible_nums[i]
        else:
            i += 1
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] > q:
            del possible_nums[i]
        else:
            i += 1
            
elif line == "BAAB":
    # Remove all between p and q
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] > p and possible_nums[i] < q:
            del possible_nums[i]
        else:
            i += 1
            
elif line == "BABA":
    if p + 1 == q:
        possible_nums = []
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] > q:
            del possible_nums[i]
        else:
            i += 1
            
elif line == "BBAA":
    # Remove all greater than p
    i = 0
    while i < len(possible_nums):
        if possible_nums[i] > p:
            del possible_nums[i]
        else:
            i += 1


if len(possible_nums) == 2:
    print(possible_nums[0], possible_nums[1])
else:
    print(-1)
