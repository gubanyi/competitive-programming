# Problem D - Is it a tree? Squirrels!
#
# Competition: CCSC-CP 2024
# Last Revised Date: 4/16/2024
# Author: Gubanyi
#
# Description: The solution uses a stack data structure
#              to navigate through a string that represents
#              a squirrel climbing a tree. Determine whether
#              the string represents a tree or not by
#              traversing the tree. Also, output the degree
#              of the tree.
#
#              Also, see problem description in PDF.


def main():
    n = int(input())

    for i in range(n):
        s = input()

        stack = ["$"]
        degrees = {}
        degree = 0

        for (j, c) in enumerate(s):
            
            # Each time you visit a character,
            # that represents an edge in the graph
            # contributing to the degree of the vertex
            if c in degrees:
                degrees[c] += 1
            else:
                degrees[c] = 1
                
            if len(stack) > 1 and c == stack[-2]:
                stack.pop()

            elif c in stack:
                degree = -1
                print(stack, j, c)
                break
            
            else:
                stack.append(c)

        if degree == -1:
            print(f"Case {i}: Not a tree")
        else:
            m = max(degrees.values())
            print(f"Case {i}: Tree of degree {m}")
    

if __name__ == "__main__":
    main()
