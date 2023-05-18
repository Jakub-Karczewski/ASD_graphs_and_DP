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
    #print(v)
    k, lim = 0, len(T[v])
    while(k < lim):
        if(not T[v][k].visit):
            T[v][k].visit = 1
            #print(T[v][k].left, T[v][k].right)
            DFS(T[v][k].left if v == T[v][k].right else T[v][k].right)
        k += 1
    set.append(v)
DFS(0)
print(set)