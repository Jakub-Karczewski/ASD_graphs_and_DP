n = int(input())
m = int(input())
M, vis = [[-1 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]
second, chuj = [[float('inf') for _ in range(n)] for _ in range(n)], [[float('inf') for _ in range(n)] for _ in
                                                                      range(n)]
T = [[[float('inf') for _ in range(n)] for _ in range(n)] for _ in range(n)]
pom = [0] * n
for i in range(n): M[i][i] = 0
par = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a = int(input())
    b = int(input())
    c = int(input())
    M[a][b], M[b][a] = c, c
    for j in range(n):
        if (j != a):
            T[b][a][j] = c
        if (j != b):
            T[a][b][j] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if (i != j):
                for l in range(n):
                    T[i][j][l] = min(T[i][j][l], T[i][k][l] + T[k][j][l])
min_cycle = float('inf')
for i in range(n):
    for j in range(n):
        if (M[i][j] > 0):
            for l in range(n):
                if (l != i and M[j][l] > 0 and T[i][l][j] + M[j][l] + M[i][j] < min_cycle):
                    min_cycle = T[i][l][j] + M[j][l] + M[i][j]
# for i in range(n):
# for j in range(n):
# print(T[i][j], end = ' ')
# print()
print(min_cycle)