#from WIET import jebaćdziekana
n = int(input())
m = int(input())
edge = []
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    edge.append([c, a, b])
edge.sort()
edge = edge[::-1]
dist = [float('inf')] * n
dist[0] = 0
for i in range(len(edge)):
    waga, x, y = edge[i]
    if(dist[x] != float('inf')):
        if(dist[x] + waga < dist[y]):
            dist[y] = dist[x] + waga
print(dist)
