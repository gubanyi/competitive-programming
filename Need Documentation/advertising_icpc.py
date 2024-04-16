

(n, m) = (int(i) for i in input().split())

grid = []

for i in range(n):
    grid.append(list(input()))


num_question = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "?":
            num_question += 1

num_ways = 0

for i in range(n-1):
    for j in range(m-1):
        if ((grid[i][j] == "I" or grid[i][j] == "?") and
            (grid[i][j+1] == "C" or grid[i][j+1] == "?") and
            (grid[i+1][j] == "P" or grid[i+1][j] == "?") and
            (grid[i+1][j+1] == "C" or grid[i+1][j+1] == "?")):

            num_question_left = num_question
            if grid[i][j] == "?":
                num_question_left -= 1
            if grid[i+1][j] == "?":
                num_question_left -= 1
            if grid[i][j+1] == "?":
                num_question_left -= 1
            if grid[i+1][j+1] == "?":
                num_question_left -= 1
            
            num_ways += 3**(num_question_left) % 998244353

print(num_ways)
