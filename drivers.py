from kol2atesty import runtests

def drivers( P, B ):
    P.append((B, True))
    n = len(P)
    for i in range(n):
        P[i] = (P[i][0], P[i][1], i)
    P.sort()
    print(P)
    n = len(P)

    dist = [x[0] for x in P]
    typ = [int(x[1]) for x in P]

    DP = [[[float('inf') for _ in range(3)] for _ in range(2)] for _ in range(n)]
    par = [[[(-1, -1, -1) for _ in range(3)] for _ in range(2)] for _ in range(n)]

    # 0 - Jacek, 1 - Marian
    # DP[i, j, k] = laczne minimum przesiadek dla mariana, gdzie aktualnie bez zmiany przejechalismy
    # k przesiadek, aktualnie jedzie kierowca j i jestesmy na indeksie i

    DP[0][0][typ[0]] = 0
    for i in range(1, n):

        if not typ[i]:
            for j in range(2):
                for k in range(3):
                    act_val = DP[i-1][j][k] + j
                    if act_val < DP[i][j][k]:
                        DP[i][j][k] = act_val
                        par[i][j][k] = (i-1, j, k)
        else:
            # przypadek kiedy mamy przesiadke ale nie zmieniamy, mozemy to zrobic tylko dla
            # aktualnej liczby przesiadek rownej mniej niz 2
            for j in range(2):
                for k in range(2):
                    act_val = DP[i-1][j][k]
                    if act_val < DP[i][j][k+1]:
                        DP[i][j][k+1] = act_val
                        par[i][j][k+1] = (i-1, j, k)

            # przypadek kiedy zmieniamy, wtedy zawsze resetujemy przesiadki,
            # mozemy zmienic w dowolnym momencie, przy dowolnej obecnej liczbie przesiadek

            for j in range(2):
                for k in range(3):
                    act_val = DP[i-1][j][k]
                    if act_val < DP[i][1-j][0]:
                        DP[i][1 - j][0] = act_val
                        par[i][1-j][0] = (i-1, j, k)

    #szukamy na ostatnim punkcie najbardziej oplacalnej sekwencji, na ktorej moglismy skonczyc
    best = (-1, -1, -1)
    min_val = float('inf')
    for j in range(2):
        for k in range(3):
            if DP[n-1][j][k] < min_val:
                best = (n-1, j, k)
                min_val = DP[n-1][j][k]


    changes = []
    #Sprawdzamy idac po parentach az dojdziemy do indeksu poczatkowego
    while best[0] > 0:
        temp = best
        x, y, z = best
        par_best = par[x][y][z]
        # dodajemy do listy zmian tylko jesli wspolrzedne sie roznia i punkt jest rozny od punktu B
        # punkt B zakladamy ze po posortowaniu bedzie zawsze na koncu
        if temp[1] != par_best[1] and P[x][2] != n-1:
            changes.append(P[x][2])
        best = par_best
    #print(changes)
    return changes


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )