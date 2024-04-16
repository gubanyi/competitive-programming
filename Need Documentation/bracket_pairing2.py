
def match_count(c1,c2):

    if (c1 in ")>}]"):
        return 0

    if (c2 in "(<{["):
        return 0
    
    if (c1 == "?" and c2 == "?"):
        return 4
    
    if (c1 == "?" or c2 == "?" or
        c1 == "(" and ")" == c2 or
        c1 == "{" and "}" == c2 or
        c1 == "[" and "]" == c2 or
        c1 == "<" and ">" == c2):
        return 1
    
    return 0

memo = {}
def count(s):
    if s in memo:
        return memo[s]

    if len(s) == 0:
        return 1

    if len(s) == 1:
        return 0

    if len(s) == 2:
        return match_count(s[0], s[1])

    c = 0
    for k in range(1, len(s)):
        mc = match_count(s[0], s[k])
        if mc > 0:
            c += count(s[1:k]) * mc * count(s[k+1:])

    memo[s] = c
    return c


print(count(input()))

