import queue
n = int(input())
m = int(input())
T = [[] for _ in range(n)]
dist, vis = [float('inf')] * n, [0] * n
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
s = int(input())
t = int(input())
Q, flag, mini = queue.PriorityQueue(), 0, float('inf')
for i in range(2):
    Q.put((0, s, flag))
    dist[s] = 0
    while(Q.qsize()):
        val, v, id = Q.get()
        if(vis[v]):
            continue
        vis[v] = 1
        for j in range(len(T[v])):
            w, y = T[v][j]
            odl = 0 if id else y
            if(not vis[w] and dist[v] + odl < dist[w]):
                dist[w] = dist[v] + odl
                Q.put((dist[w], w, not id))
    mini = min(dist[t], mini)
    for k in range(n):
        dist[k] = float('inf')
        vis[k] = 0
    flag = not flag
print(mini)