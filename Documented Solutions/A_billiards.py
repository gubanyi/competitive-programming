# Problem A: Bouncy Billiard Balls
#
# Competition: CCSC-CP 2024
# Last Revised Date: 4/16/2024
# Author: Gubanyi
#
# Description: The solution abstracts the problem into a
#              different topological space than the
#              billiards board. Instead of the ball bouncing
#              off walls, the solution has the ball cross
#              over boundaries and counts "bounces" by
#              crossing boundaries. This makes the simulation
#              much simpler, using modular arithmetic to
#              model the billiards board.

def main():
    n = int(input())

    for case in range(1,n+1):
        bounce = 0
        
        (start_x, start_y) = (int(x) for x in input().split())

        (dx, dy) = (int(x) for x in input().split())

        current_x = start_x + dy
        current_y = start_y + dy

        while start_x != current_x % 176 and start_y != current_y % 88:
            # Check for crossing/bouncing boundary
            if current_x // 88 > (current_x - dx) // 88:
                bounce += 1
            if current_y // 44 > (current_y - dy) // 44:
                bounce += 1

            current_x = current_x + dx
            current_y = current_y + dy

        # Check for crossing/bouncing boundary
        if current_x // 88 > (current_x - dx) // 88:
            bounce += 1
        if current_y // 44 > (current_y - dy) // 44:
            bounce += 1

        print(f"Case {case}: {bounce}")

if __name__ == "__main__":
    main()
