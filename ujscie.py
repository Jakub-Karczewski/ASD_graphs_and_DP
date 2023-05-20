n = int(input())
m = int(input())
T = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    T[a][b] = 1
x, y = 0, 0
while(x < n and y < n):
    while(y < n and not T[x][y]):
        print(x, y)
        y += 1
    if(y == n):
        break
    while(x < n and T[x][y]):
        print(x, y)
        x += 1
flag = 0
if(y == n):
    flag = 1
    for i in range(n):
        if(T[x][i] or (i != x and not T[i][x])):
            flag = 0
            break
if(flag):
    print("Istnieje zrodlo")
else:
    print("Nie istnieje zrodlo")
