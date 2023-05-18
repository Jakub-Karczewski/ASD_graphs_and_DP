from collections import deque
kolejka = deque()
n = int(input())
m = int(input())
list = [[] for _ in range(n)]
vis = [0] * n
color = [-1] * n
print(list)
for i in range (m):
    a = int(input())
    b = int(input())
    list[a].append(b)
    list[b].append(a)
print(list)
#print(list[0][1])
flag = 0
while(True):
    found = 0
    for j in range(n):
        if(not vis[j]):
            found, first = 1, j
            break
    if(not found):
        break
    kolejka.append(first)
    vis[first], color[0] = 1, 0
    while(len(kolejka)):
        act = kolejka.popleft()
        for i in range(len(list[act])):
            x = list[act][i]
            if(not vis[x]):
                vis[x] = 1
                color[x] = 1 - color[act]
                kolejka.append(x)
            elif(color[x] == color[act]):
                flag = 1
                break
    if(flag):
        break
if(not flag):
    print("dwudzielny")
else:
    print("NIE")
