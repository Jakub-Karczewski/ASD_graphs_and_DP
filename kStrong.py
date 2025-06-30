
from egz1btesty import runtests
# Autor: Jakub Krupa, ja tylko rzucalem pomysly
# f(i,u) - maksymalna suma przedziału kończącego się na i, przy u maksymalnych usunięciach
# f(i,u) = max(f(i-1,u) + T[i], T[i]) albo dodajemy element do ciągu, albo zaczynamy nowy
# f(i,u) = max(f(i,u), f(i-1,u-1)) lub pomijamy ity element i wykorzystujemy usunięcie

def kstrong(T, k):
    n = len(T)
    dp = [[float('-inf')] * (k + 1) for _ in range(n)]
    
    for u in range(k + 1):
        dp[0][u] = 0 if u > 0 else T[0]

    for j in range(1, n):
        for u in range(k + 1):
            dp[j][u] = dp[j-1][u] + T[j]
            if u > 0:
                dp[j][u] = max(dp[j][u], dp[j-1][u-1])
            if u == 0:
                dp[j][u] = max(dp[j][u], T[j])
            else:
                dp[j][u] = max(dp[j][u], 0)

    
    return max(max(row) for row in dp) # bo mozemy w pewnym momencie dopisywać gorsze liczby i przez to największa suma jest w środku tablicy a nie na końcu
    # f(i,k) to maksymalne sumy przedziału kończące się na i, przy czym ilość wartości w środku przedziału moze być na tyle niekorzystna, ze ta maksymalna suma zostanie gdzieś w środku



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
