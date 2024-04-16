
def match_count(i,j):

    if (s[i] in ")>}]"):
        return 0

    if (s[j] in "(<{["):
        return 0
    
    if (s[i] == "?" and s[j] == "?"):
        return 4
    
    if (s[i] == "?" or s[j] == "?" or
        s[i] == "(" and ")" == s[j] or
        s[i] == "{" and "}" == s[j] or
        s[i] == "[" and "]" == s[j] or
        s[i] == "<" and ">" == s[j]):
        return 1
    
    return 0

memo = {}
def subproblem(i,j):
    if (i,j) in memo:
        return memo[(i,j)]

    if (i > j):
        return 1

    if (i == j):
        return 0

    if (i+1 == j):
        return match_count(i,j)

    c = 0
    for k in range(i+1, j+1):
        c += subproblem(i+1, k-1) * match_count(i,k) * subproblem(k+1,j)

    memo[(i,j)] = c
    return c


s = input()
print(subproblem(0,len(s)-1))
