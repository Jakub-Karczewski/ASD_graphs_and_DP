from zad2testy import runtests
#Jakub Karczewski
#Wybieramy zbior elementow bo wiemy ze mozemy je brac jeden po drugim, bez koniecznosci przerw, obojetnie w jakiej kolejności, nawet jakbysmy szli tylko z 1 strony bylaby taka sama sytuacja
#Interesuje nas jedynie zbior który zostanie wybrany, zaczynamy od najwiekszych i je dobieramy, bo wtedy mamy max zysk, każdy nowy dodany powoduje
#ze w ktoryms momencie ilosc sniegu spadnie nam dodatkowo o k, jesli zostało wybranych już k liczb, czyli on sam musi miec wartosc przynajmniej k+1
#Nie bierzemy pod uwage kolejnosci wybierania, bo biorac np 5 elementow zawsze nastapi nam ogolny spadek o (5+1)*5/2, a elementy mozemy sobie dobierac bezposrednio jeden po drugim dzieki temu warunkowi,
#ze ciezarowka moze w danej chwili podjechac dowolnie daleko
#sortujemy i bierzemy od najwiekszych dopoki mamy profit dodatni
#Korzystamy w heapsorta max dzieki ktoremu uzyskujemy po kolei elementy od najwiekszego do najmniejszego, przez co mozemy, w pewnym momencie przerwac jesli warunek jest niespelniony, bo nie ma juz potrzeby
#sortowania calej tablicy


def snow( S ):
    rozm = len(S)
    def heapify(ind, N):
        left = 2 * ind + 1
        right = 2 * ind + 2
        maxi = ind
        if (left < N and S[left] > S[ind]):
            maxi = left
        if (right < N and S[right] > S[maxi]):
            maxi = right
        if (maxi != ind):
            S[ind], S[maxi] = S[maxi], S[ind]
            heapify(maxi, N)
    last = rozm // 2 - 1
    for y in range(last, -1, -1):
        heapify(y, rozm)
    minus, wyn = 0, 0
    for i in range(rozm - 1, -1, -1):
        if(S[0] < minus+1):
            break
        wyn += S[0]
        S[0], S[i] = S[i], S[0]
        heapify(0, i)
        minus += 1
    minus -= 1
    wyn -= (minus) * (minus+1)//2
    return wyn

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
