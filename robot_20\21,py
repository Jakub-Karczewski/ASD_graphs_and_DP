from zad2testy import runtests
from queue import PriorityQueue


def robot(L, A, B):
    n = len(L)
    m = len(L[0])

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    A1 = (A[1], A[0])
    B1 = (B[1], B[0])
    a, o = 3, 4
    dist = [[[[float('inf') for _ in range(o)] for _ in range(a)] for _ in range(m)] for _ in range(n)]
    vis = [[[[False for _ in range(o)] for _ in range(a)] for _ in range(m)] for _ in range(n)]
    delta_o = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    delta_acc = [60, 40, 30]
    Q = PriorityQueue()
    Q.put((0, (A1[0], A1[1], 0, 0)))
    while (not Q.empty()):
        val, param = Q.get()
        x, y, acc, orient = param
        if(vis[x][y][acc][orient]):
            continue
        vis[x][y][acc][orient] = True
        new_x, new_y = x + delta_o[orient][0], y + delta_o[orient][1]

        if is_valid(new_x, new_y) and L[new_x][new_y] != "X":
            if acc < 2 and not vis[new_x][new_y][acc + 1][orient]:
                if val + delta_acc[acc] < dist[new_x][new_y][acc + 1][orient]:
                    dist[new_x][new_y][acc + 1][orient] = val + delta_acc[acc]
                    Q.put((val + delta_acc[acc], (new_x, new_y, acc + 1, orient)))
            else:
                if val + 30 < dist[new_x][new_y][2][orient] and not vis[new_x][new_y][2][orient]:
                    dist[new_x][new_y][2][orient] = val + 30
                    Q.put((val + 30, (new_x, new_y, 2, orient)))

        for i in range(-1, 2, 2):
            if val + 45 < dist[x][y][0][(orient + i) % 4] and not vis[x][y][0][(orient + i) % 4]:
                dist[x][y][0][(orient + i) % 4] = val + 45
                Q.put((val + 45, (x, y, 0, (orient + i) % 4)))

    ans = float('inf')
    for i in range(a):
        for j in range(o):
            ans = min(ans, dist[B1[0]][B1[1]][i][j])

    return ans if ans != float('inf') else None

runtests(robot)
