# No need for imports, as Python's built-in modules handle the required functionality directly

# Define a function to check if a cell is valid
def is_valid(xc, yc, x, y):
    return 0 <= xc < x and 0 <= yc < y

# Define a class for the cell structure
class Cell:
    def __init__(self, x, y, is_black):
        self.x = x
        self.y = y
        self.visited = 0
        self.is_black = is_black

# Main function
def main():
    # Input dimensions
    y, x = map(int, input().split())
    count = 0

    # Initialize matrix and list of cells
    mat = [[None for _ in range(y)] for _ in range(x)]
    vc = []

    # Input matrix and initialize cells
    for j in range(y):
        s = input()
        for i in range(len(s)):
            tcell = Cell(i, j, s[i] == '#')
            mat[i][j] = tcell
            if tcell.is_black:
                vc.append(tcell)

    # Process connected components
    if vc:
        vi = 0
        while vi < len(vc):
            if mat[vc[vi].x][vc[vi].y].visited == 1:
                vi += 1
            else:
                stack = [vc[vi]]
                while stack:
                    tcell = stack.pop()
                    if mat[tcell.x][tcell.y].visited == 0:
                        mat[tcell.x][tcell.y].visited = 1
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                if dx != 0 or dy != 0:
                                    if is_valid(tcell.x + dx, tcell.y + dy, x, y) and mat[tcell.x + dx][tcell.y + dy].is_black:
                                        stack.append(mat[tcell.x + dx][tcell.y + dy])
                count += 1
    print(count)

# Call the main function
if __name__ == "__main__":
    main()
