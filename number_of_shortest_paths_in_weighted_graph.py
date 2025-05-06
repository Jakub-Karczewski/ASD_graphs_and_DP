n = int(input())
m = int(input())
T, vis = [[-1 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]
#T to bedzie graf skierowany wazony w reprezentacji macierzowej
act = [1] * n
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a][b] = c
dist, ile = [float('inf')] * n, [0] * n
s, t = 0, n-1
ile[s], dist[s] = 1, 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            new = dist[i] + T[i][j]
            if(dist[i] != float('inf') and T[i][j] != -1 and new <= dist[j]):
                if(new == dist[j] and vis[j][i] != act[j]):
                    ile[j] += ile[i]
                    vis[j][i] = act[j]
                elif(new < dist[j]):
                    ile[j] = ile[i]
                    act[j] += 1
                    vis[j][i] = act[j]
                dist[j] = new
print(dist)
print(ile)
