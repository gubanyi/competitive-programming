class Graph:
    def __init__(self, vertices=[]):
        self.V = vertices
        self.E = []
    def add_edge(self, x, y):
        self.E.append( (x, y) )

    def match(self):
        matching
        while len(matched) < len(self.V)//2:
            
        return matched

parent = {s:None}
adj = {}
def dfs(s):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs(v)
        


(n, k) = ( int(x) for x in input().split() )

rows = []
for _ in range(k):
    row = [int(x) for x in input().split()]
    rows.append(row)

impossible = False
for r in range(k):
    s = set()    
    for c in range(n):
        if rows[r][c] in s:
            impossible = True
        else:
            s.add(rows[r][c])



for c in range(n):
    s = set()
    for r in range(k):
        if rows[r][c] in s:
            impossible = True
        else:
            s.add(rows[r][c])

if impossible:
    print("no")
else:
    print("yes")

    while len(rows) < n:
        # TODO: Build each missing row with bipartite matching
            
                
                
                
