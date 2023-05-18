import random, math
from queue import PriorityQueue
Q = PriorityQueue()
n = int(input())
m = int(input())
T = [[] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    T[a].append([b, c])
    T[b].append([a, c])
print("Lista somsiadow:")
print(T)
print()
odl = [math.inf] * n
odl[0] = 0
par, vis  = [-1] * n, [0] * n
Q.put((0, 0))
while(Q.qsize()):
    prior, chuj = Q.get()
    print(chuj)
    if(vis[chuj]):
        continue
    vis[chuj] = 1
    for i in range(len(T[chuj])):
        new, dist = T[chuj][i]
        if(not vis[new] and odl[new] > odl[chuj] + dist):
            odl[new] = odl[chuj] + dist
            par[new] = chuj
            Q.put((odl[new], new))
print("\n")
print("Odleglosc od zrodla:")
print(odl)


