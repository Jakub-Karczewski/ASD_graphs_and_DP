from zad9testy import runtests

def min_cost( O, C, T, L ):
    n = len(C)
    S = [[0, 0] for _ in range(n)]
    for i in range(n):
        S[i] = O[i], C[i]
    S.sort()
    DP = [[-1, -1] for _ in range(n+1)]
    #print(S)
    def func(i, used):
        if (S[i][0] <= T):
            DP[i][used] = S[i][1]
            return S[i][1]
        if (DP[i][used] != -1):
            return DP[i][used]
        dist_i = S[i][0]
        mini = float('inf')
        for j in range(i - 1, -1, -1):
            dist_j = S[j][0]
            if (dist_i != dist_j and dist_i - dist_j <= T):
                mini = min(mini, S[i][1] + deepthroat(j, used))
            elif (dist_i - dist_j > T):
                break
        if (not used):
            if (S[i][0] <= 2 * T):
                DP[i][used] = S[i][1]
                return S[i][1]
            for j in range(i - 1, -1, -1):
                dist_j = S[j][0]
                if (T < dist_i - dist_j <= 2 * T):
                    mini = min(mini, S[i][1] + deepthroat(j, 1))
                elif (dist_i - dist_j > 2 * T):
                    break
        DP[i][used] = mini
        return mini

    S.append([L, 0])
    wyn = func(n, 0)
    return wyn


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
