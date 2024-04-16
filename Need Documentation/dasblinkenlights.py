(p,q,s) = (int(x) for x in input().split())

works = False

for i in range(1, s+1):
    if i%p == 0 and i%q == 0:
        works = True
        break


if works:
    print("yes")
else:
    print("no")
