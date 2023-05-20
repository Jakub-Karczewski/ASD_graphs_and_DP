import collections
def abs(a):
    return a if a > 0 else (-1)*a
n = int(input())
p = [0] * n
for i in range(n):
    p[i] = int(input())
k = int(input())
vis = [0] * n
kolej = collections.deque()
kolej.append(0)
flag = 0
while(len(kolej)):
    w = kolej.popleft()
    #print(p[w])
    if(w == n-1):
        flag = 1
        break
    vis[w] = 1
    for i in range(n):
        if(not vis[i] and abs(p[i] - p[w]) <= k):
            kolej.append(i)
if(flag):
    print("Da sie doleciec")
else:
    print("Nie da sie doleciec")