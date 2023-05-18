n = int(input())
m = int(input())
global czas
czas = 1
T = [[] for _ in range(n)]
time, par, vis, dist = [-1] * n, [-1] * n, [0] * n, [float('inf')] * n
sorted = []
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
def topological(w):
    vis[w] = 1
    global czas
    for j in range(len(T[w])):
        x = T[w][j][0]
        if(not vis[x]):
            par[x] = w
            topological(x)
    time[w] = czas
    sorted.append(w)
    czas += 1
topological(0)
sorted = sorted[::-1]
print(sorted)
dist[0] = 0
for i in range(n):
    chuj = sorted[i]
    if(dist[chuj] == float('inf')):
        continue
    for j in range(len(T[chuj])):
        boy, val = T[chuj][j]
        if(dist[chuj] + val < dist[boy]):
            dist[boy] = dist[chuj] + val
print(dist)