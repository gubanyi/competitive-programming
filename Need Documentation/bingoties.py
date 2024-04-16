

n = int(input())
cards = []
num_counts = {}
for i in range(n):
    card = []
    for i in range(5):
        line = input()
        nums = {int(x) for x in line.split()}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
        card.append(nums)

    try:
        input()
    except:
        pass

    cards.append(card)

tie_pairs = []
for num in num_counts:
    if num_counts[num] > 1:
        for i in range(n):
            for row in cards[i]:
                if num in row:
                    for j in range(i+1, n):
                        for row2 in cards[j]:
                            if num in row2:
                                union = row.union(row2)
                                union.discard(num)
                                has_bingo = False
                                for k in range(n):
                                    if k != i and k != j:
                                        for row3 in cards[k]:
                                            if row3.issubset(union):
                                                has_bingo = True
                                if not has_bingo:
                                    tie_pairs.append( (i+1, j+1) )
                                

if len(tie_pairs) == 0:
    print('no ties')
else:
    tie_pairs.sort()
    print(tie_pairs[0][0], tie_pairs[0][1])
