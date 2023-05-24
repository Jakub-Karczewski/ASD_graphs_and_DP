n = int(input())
m = int(input())
T = [[] for _ in range(n)]
s = 0
low, par, vis, czas = [float('inf')] * n, [-1] * n, [0] * n, [-1] * n
for i in range(m):
    a = int(input())
    b = int(input())
    T[a].append(b)
    T[b].append(a)
def DFS(w, time):
    vis[w], czas[w] = 1, time
    low[w] = time
    for i in range(len(T[w])):
        v = T[w][i]
        if(not vis[v]):
            par[v] = w
            DFS(v, time + 1)
        elif(v != par[w]):
            low[w] = min(low[w], low[v])
    for i in range(len(T[w])):
        v = T[w][i]
        if(v != par[w]):
            low[w] = min(low[w], low[v])
DFS(0, 1)
print(low)
print(czas)
print("mosty:")
for i in range(n):
    if(i != s and vis[i] != 2 and low[i] == czas[i]):
        vis[i] = 2
        print("(", par[i],'', i, ")")

