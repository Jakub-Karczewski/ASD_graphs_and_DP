from collections import deque
def rek(s, d, prev):
    if(d != s):
        rek(s, prev[d], prev)
    print(d)
kolej = deque()
n = int(input())
m = int(input())
prev, vis = [-1] * n, [0] * n
list = [[] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    list[a].append(b)
    list[b].append(a)
s = int(input())
d = int(input())
kolej.append(s)
vis[s] = 1
while(len(kolej)):
    act = kolej.popleft()
    for i in range(len(list[act])):
        w = list[act][i]
        if(not vis[w]):
            prev[w] = act
            vis[w] = 1
            kolej.append(w)
ind = d
print('')
if(not vis[d]):
    print("Nieosiagalny")
else:
    rek(s, d, prev)
    print('')
    while(ind != s):
        print(ind)
        ind = prev[ind]
    print(s)


