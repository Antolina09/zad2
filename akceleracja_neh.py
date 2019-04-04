czasy_na_maszynach = [[1,4,3,2,1],[1,1,4,4,2],[3,2,3,1,3]]
ilosc_maszyn = 3
ilosc_zadan = 5

def czytanie_z_pliku(plik_do_wczytania):
    tablica=[]
    text_file = open(plik_do_wczytania, "r+")
    for line in text_file.readlines():
         tablica.extend(line.split())
    ilosc_zadan=  int(tablica[0])
    ilosc_maszyn= int(tablica[1])
    index=2
    print("ilosc zadan",ilosc_zadan)
    print("ilosc maszyn",ilosc_maszyn)
    zadania_dla_maszyn = [[] for i in range(int(ilosc_maszyn))]

    while index < (ilosc_maszyn*ilosc_zadan +2):
        for k in range(ilosc_maszyn):
            zadania_dla_maszyn[k].append(int(tablica[index]))
            index+=1
    text_file.close()
    return zadania_dla_maszyn, ilosc_zadan, ilosc_maszyn

def takeFirst(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[0]
def takeSec(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[1]

def przepisanie_wart(tab):
    tab_temp = [[] for i in range(len(tab))]
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab_temp[i].insert(j,tab[i][j])
    return tab_temp

def kolejnoscNeh(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan):
    suma_zadan = []
    suma_zadan_z_czasami = []
    sum = 0
    tab_zadan=[]
    for ind in range(ilosc_zadan):
        for i in range(ilosc_maszyn):
            sum += int(czasy_na_maszynach[i][ind])
        suma_zadan.append(sum)
        sum = 0
    #print(suma_zadan)  # nieposortowana
    for i in range(len(suma_zadan)):
        suma_zadan_z_czasami.append([suma_zadan[i], i])
    suma_sort = sorted(suma_zadan_z_czasami,key=takeFirst, reverse=True)
    for i in range(ilosc_zadan):
        tab_zadan.append(takeSec(suma_sort[i]))
    return tab_zadan, suma_sort

#tab_zadan = kolejnoscNeh(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan)[0]
#kol =[0,2,1,3]
kolejnosc = kolejnoscNeh(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan)[0]
def najdluzsza_dochodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan,kolejnosc):
    macierz_pom = [[]for i in range(ilosc_maszyn)]
    for i in range(ilosc_maszyn):
        macierz_pom[i].insert(0,0)
        macierz_pom[i].insert(1,czasy_na_maszynach[i][kolejnosc[0]])
    for i in range(ilosc_zadan):
        macierz_pom[0].insert(i+1,macierz_pom[0][i]+czasy_na_maszynach[0][kolejnosc[i]])
    for i in range(1,ilosc_maszyn):
        for j in range(1,ilosc_zadan+1):
            macierz_pom[i].insert(j,max(macierz_pom[i-1][j],macierz_pom[i][j-1]) + czasy_na_maszynach[i][kolejnosc[j-1]])
    for i in range(ilosc_maszyn):
        macierz_pom[i].pop(-1)
    return macierz_pom

def najdluzsza_wychodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan,kolejnosc):
    odwrocone_maszyny = czasy_na_maszynach[::-1]
    odwrocona_kolejnosc = kolejnosc[::-1]
    macierz_pom = [[]for i in range(ilosc_maszyn)]
    for i in range(ilosc_maszyn):
        macierz_pom[i].insert(0,0)
        macierz_pom[i].insert(1,odwrocone_maszyny[i][odwrocona_kolejnosc[0]])
    for i in range(ilosc_zadan):
        macierz_pom[0].insert(i+1,macierz_pom[0][i]+odwrocone_maszyny[0][odwrocona_kolejnosc[i]])
    for i in range(1,ilosc_maszyn):
        for j in range(1,ilosc_zadan+1):
            macierz_pom[i].insert(j,max(macierz_pom[i-1][j],macierz_pom[i][j-1]) + odwrocone_maszyny[i][odwrocona_kolejnosc[j-1]])
    for i in range(ilosc_maszyn):
        macierz_pom[i].pop(-1)
    return macierz_pom

def Neh(czasy_na_maszynach,ilosc_maszyn, ilosc_zadan):
    kolejnosc = kolejnoscNeh(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan)[0]
    odwrocona_kolejnosc = kolejnosc[::-1]
    odwrocone_maszyny = czasy_na_maszynach[::-1]
    kol = kolejnosc[:2]
    od_kol = kol[::-1]
    doch1 = najdluzsza_dochodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,2,kol)
    wych1 = najdluzsza_wychodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,2,kol)
    doch2 = najdluzsza_dochodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,2,od_kol)
    wych2 = najdluzsza_wychodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,2,od_kol)
    print("doch1", doch1, "wych1", wych1, "doch2", doch2, "wych2", wych2)
    cmax1 = doch1[-1][-1]
    cmax2 = doch2[-1][-1]
    if cmax1 <= cmax2:
        doch, wych = doch1, wych1[::-1]
    else:
        doch, wych = doch2, wych2[::-1]
    cmax = min(cmax1,cmax2)
    print("doch", doch,"wych", wych)
    print("kol", kolejnosc, "czasy na m" ,czasy_na_maszynach)

    for i in range(3,ilosc_zadan+1):
        indeks_kolejnosci = 0
        for k in range(i):
            pom = []
            for j in range(ilosc_maszyn):
                if j == 0:
                    doch[j].insert(k+1,doch[j][k]+czasy_na_maszynach[j][kolejnosc[i-1]])
                    pom.append(doch[j][k+1])
                else:
                    doch[j].insert(k+1,max(doch[j][k],doch[j-1][k+1])+czasy_na_maszynach[j][kolejnosc[i-1]])
                    pom.append(doch[j][k+1])
            print("d", doch, "p", pom)
            for p in range(len(pom)):
                    pom[p] += wych[p][-(k+1)]
            pom.sort()
            if k == 0:
                cmax = pom[-1]
                indeks_kolejnosci = k
                print(cmax)
            else:
                cmaxn = pom[-1]
                if cmaxn < cmax:
                    cmax = cmaxn
                    indeks_kolejnosci = k
                    print(cmax)
            print("pom2", pom, "in", indeks_kolejnosci)
            for g in range(j+1):
                doch[g].pop(k+1)
        
        kol.insert(indeks_kolejnosci,kolejnosc[i-1])
        print("kol", kol)
        doch = najdluzsza_dochodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,i,kol)
        wych = najdluzsza_wychodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,i,kol)
    print(kol, cmax)
    
    
#najdluzsza_dochodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan,kolejnosc)
#najdluzsza_wychodzaca_sciezka(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan,kolejnosc)
czasy_na_maszynach2, ilosc_z, ilosc_m = czytanie_z_pliku("ta01.txt")
#Neh(czasy_na_maszynach2,ilosc_m,ilosc_z)
Neh(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan)