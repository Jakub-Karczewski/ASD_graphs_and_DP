n = int(input())
m = int(input())
T, vis, edge_vis sorted_by_time = [[] for _ in range(n)], [0] * n, [[] for _ in range(n)]
G = [[] for _ in range(n)]
def odwroc():
    for i in range(n):
        for j in range(len(T[i])):
            x = T[i][j]
            G[x].append(i)
def DFG(graph, w):
    vis
for i in range(m):
    a = int(input())
    b = int(input())
    T[a].append(b)
