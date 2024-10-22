# Title: Lone Rook with BFS (Incomplete)
# Author: Gubanyi
# Date: 10/21/2024
#
# Description: Implements a BFS to solve the Lone Rook problem. However, this program does not
#              implement functionality to handle for when the Rook captures Knights. Thus, the
#              program is incomplete and solves only two of the three sample test cases correctly.
#
# Problem: https://cune.kattis.com/courses/CPT/CPT24-25/assignments/ypv94q/problems/lonerook
#
# Solution Description from ICPC Archive:
# This problem can be solved in a BFS fashion. We maintain a queue to process the cells
# reachable by the rook. A cell is reachable if a rook can eventually move to it safely after
# removing all its attacking knights. We preprocess for each cell how many knights attack it
# as attacked[i][j]. Whenever a reachable cell c is popped from the queue, we do the following:
#   • If c has a knight, then we remove that knight and reduce attacked[i][j] of those cells
#     attacked by this knight. If any of them, say c', becomes no longer attacked, then go in
#     four directions from c' to find a cell reachable by rook. If such a cell exists, then we
#     add c to the queue. This step takes O(8 · 2(r + c)) time.
#   • Go in four directions and add all cells to the queue until we hit a knight. If this knight
#     is attacked, we stop. Otherwise we add the knight’s cell to the queue and stop. This
#     step takes O(2(r + c)) time.
# Every time we add a cell to the queue, we mark that cell as reachable. Each cell will be
# added to the queue exactly once. The total running time is O(8 · 2(r + c)rc).


# Needed for BFS
from collections import deque


# Input dimensions and board
inputs = input().split()
rows = int(inputs[0])
cols = int(inputs[1])
board = [input() for i in range(rows)]


# Need to build a board for how many times each location
# is attacked by a knight. A safe space isn't attacked.
def attacks(i,j):
    attacks = 0
    # Check each of 8 possible positions where
    # a knight could attack (i,j)
    if i-1 >= 0 and j-2 >= 0 and board[i-1][j-2] == "K":
        attacks += 1
    if i-1 >= 0 and j+2 < cols and board[i-1][j+2] == "K":
        attacks += 1
    if i+1 < rows and j-2 >= 0 and board[i+1][j-2] == "K":
        attacks += 1
    if i+1 < rows and j+2 < cols and board[i+1][j+2] == "K":
        attacks += 1
    if i-2 >= 0 and j-1 >= 0 and board[i-2][j-1] == "K":
        attacks += 1
    if i-2 >= 0 and j+1 < cols and board[i-2][j+1] == "K":
        attacks += 1
    if i+2 < rows and j-1 >= 0 and board[i+2][j-1] == "K":
        attacks += 1
    if i+2 < rows and j+1 < cols and board[i+2][j+1] == "K":
        attacks += 1
    
    return attacks


# vertices
A = [ [ 0 for i in range(cols)] for i in range(rows) ]

for i in range(rows):
    for j in range(cols):

        A[i][j] = attacks(i,j)

        if board[i][j] == 'T':
            target = (i,j)

        if board[i][j] == 'R':
            start = (i,j)

# Use function for simple return early when found
def bfs():
    queue = deque([start])  
    visited = set()  # to track visited nodes
    visited.add(start)
    
    # Helper function to check if a cell is valid
    def is_valid(i, j):
        return 0 <= i < rows and 0 <= j < cols and A[i][j] == 0 and (i, j) not in visited
    
    
    while queue:
        current = queue.popleft()
        # Tracing statement for debugging purposes
        #print(current)
        if current == target:
            return True
        
        i, j = current

        # Explore all possible DOWN moves of a rook from this position
        #   -> adding all valid moves, up to a knight, to the queue
        new_i = i+1
        hit_knight = False
        while new_i < rows and not hit_knight:
            if board[new_i][j] == "K":
                hit_knight = True

            if is_valid(new_i, j):
                queue.append((new_i, j))
                visited.add((new_i, j))   
                
            new_i += 1

        # Explore all possible UP moves of a rook from this position
        #   -> adding all valid moves, up to a knight, to the queue
        new_i = i-1
        hit_knight = False
        while new_i >= 0 and not hit_knight:
            if board[new_i][j] == "K":
                hit_knight = True
                
            if is_valid(new_i, j):
                queue.append((new_i, j))
                visited.add((new_i, j))
                
            new_i -= 1

        # Explore all possible LEFT moves of a rook from this position
        #   -> adding all valid moves, up to a knight, to the queue
        new_j = j-1
        hit_knight = False
        while new_j >= 0 and not hit_knight:
            if board[i][new_j] == "K":
                hit_knight = True

            if is_valid(i, new_j):
                queue.append((i, new_j))
                visited.add((i, new_j))

            new_j -= 1

        # Explore all possible RIGHT moves of a rook from this position
        #   -> adding all valid moves, up to a knight, to the queue
        new_j = j+1
        hit_knight = False
        while new_j < cols and not hit_knight:
            if board[i][new_j] == "K":
                hit_knight = True
                
            if is_valid(i, new_j):
                queue.append((i, new_j))
                visited.add((i, new_j))
                
            new_j += 1
    
    # Return False if queue is empty because no path was found
    return False

if bfs():
    print('yes')
else:
    print('no')
