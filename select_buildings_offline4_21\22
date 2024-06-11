from zad4testy import runtests

def select_buildings(T,p):
    n = len(T)
    M = [[0, 0, 0, 0, 0] for _ in range(n)]
    for i in range(n):
        h, a, b, w = T[i]
        M[i] = b, a, h, w, i

    par = [[[-1, -1] for _ in range(p + 1)] for _ in range(n + 1)]
    M.sort()
    max_d = M[n - 1][0]
    M.append([max_d + 1, max_d + 1, 0, 0])
    # print(T)
    DP = [[-1 for _ in range(p + 1)] for _ in range(n + 1)]

    def solve(i, price):
        # print(i, price)
        if (DP[i][price] != -1):
            return DP[i][price]
        x2, x1, h1 = M[i][0], M[i][1], M[i][2]
        maxi = h1 * (x2 - x1)
        for j in range(i - 1, -1, -1):
            b, a, x = M[j][0], M[j][1], M[j][3]
            # print(j, a, b, x)
            if (b < x1 and price + x <= p):
                JD = h1 * (x2 - x1) + solve(j, price + x)
                if (JD > maxi):
                    par[i][price] = j, price + x
                    maxi = JD
        DP[i][price] = maxi
        return maxi

    res = solve(n, 0)
    #print(res)
    x, x_p = par[n][0]
    tab = []
    while (x != -1):
        tab.append(M[x][4])
        x, x_p = par[x][x_p]
    #tab.reverse()
    tab.sort()
    return tab


runtests( select_buildings, True )
