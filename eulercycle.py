class Edge:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.visit = 0
n = int(input())
m = int(input())
T, set = [[] for _ in range(n) ], []
last = [0] * n
for i in range(m):
    a = int(input())
    b = int(input())
    krawedz = Edge(a, b)
    T[a].append(krawedz)
    T[b].append(krawedz)
def DFS(v):
    lim = len(T[v])
    while(last[v] < lim):
        k = last[v]
        last[v] += 1
        if(not T[v][k].visit):
            T[v][k].visit = 1
            DFS(T[v][k].left if v == T[v][k].right else T[v][k].right)
    set.append(v)
DFS(0)
print(set)