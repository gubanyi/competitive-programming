# Programming Practice - Oct 10, 2023
#
# Code copied and edited from
# https://www.altcademy.com/blog/count-the-number-of-simple-cycles-in-a-graph

# Code uses DFS

from collections import defaultdict

count = 0

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited, stack):
        global count
        visited[vertex] = True
        stack.append(vertex)

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
            elif len(stack) > 0 and neighbor == stack[0]:
                #print("Cycle found:", stack + [neighbor])
                count += 1

        stack.pop()
        visited[vertex] = False

    def count_simple_cycles(self):
        visited = [False] * (self.V + 1)
        stack = []

        for vertex in range(1, self.V + 1):
            self.dfs(vertex, visited, stack)
            visited[vertex] = True

if __name__ == "__main__":
    m = int(input())
    g = Graph(m)
    n = int(input())
    for _ in range(n):
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        g.add_edge(x,y)    
    

    g.count_simple_cycles()
    print(count)
