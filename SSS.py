n = int(input())
m = int(input())
T, vis, edge_vis, sorted_t = [[] for _ in range(n)], [0] * n, [[] for _ in range(n)], []
G = [[] for _ in range(n)]

def odwroc():
    for i in range(n):
        for j in range(len(T[i])):
            x = T[i][j]
            G[x].append(i)

color = [0] * n
col = 1
def DFS(graph, w, add):
    vis[w] = 1
    if (add):
        sorted_t.append(w)
    print(w)
    print(graph[w])
    color[w] = col
    for j in range(len(graph[i])):
        v = graph[i][j]
        if(not vis[v]):
            DFS(graph, v, add)

for i in range(m):
    a = int(input())
    b = int(input())
    T[a].append(b)

found = 1
DFS(T, 0, 1)
odwroc()
for i in range(n):
    vis[i] = 0
k, col = 0, 1
print(sorted_t)
while(k < n):
    x = sorted_t[k]
    if(not vis[x]):
        DFS(G, x, 0)
        print()
    k += 1
    col += 1
print(T)
print(G)
print(color)