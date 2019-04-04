def czytanie_z_pliku(plik_do_wczytania):
    tablica=[]
    text_file = open("ta000.txt", "r+")
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
            zadania_dla_maszyn[k].append(tablica[index])
            index+=1
    text_file.close()
    return zadania_dla_maszyn, ilosc_zadan, ilosc_maszyn

def takMax(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return max(elem)
def takeFirst(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[0]
def takeSec(elem):  # funkcja zwracjaca drugi element w tablicy dwuwymiarowej (potrzebna do polaczenia zadan z czasem)
    return elem[1]

def Cmax(lista, ilosc_maszyn):
    czas=[0] #czas poczatkowy dla kazdej maszyny
    for i in range(len(lista)-1):
        czas.append(int(lista[i][0])+czas[i])
    #print("to czasy poczatkowe na maszynach",czas)
    for ind in range(len(lista[0])):
        czas[0] += int(lista[0][ind])
        for k in range(ilosc_maszyn-1):
            if czas[k] > czas[k+1]:
                czas[k+1]=czas[k]
            czas[k + 1] += int(lista[k + 1][ind])
    #print("to czasy koncowe na maszynach",czas)
    #print('Cmax',max(czas))
    return max(czas)


def NehInsertion(kolejnosc,nr_zadania,wartosc_czasu):
    nowa_kolejnosc=[]
    nowa_kolejnosc.extend(kolejnosc)
    nowa_kolejnosc.insert(nr_zadania,wartosc_czasu)
    return nowa_kolejnosc

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

def przepisanie_wart(tab):
    tab_temp = [[] for i in range(len(tab))]
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab_temp[i].insert(j,tab[i][j])
    return tab_temp

def Neh(czasy_na_maszynach,ilosc_maszyn, ilosc_zadan):
    tab_zadan, suma_sort = kolejnoscNeh(czasy_na_maszynach,ilosc_maszyn,ilosc_zadan)
    print("kolejnosc zadan",(tab_zadan), "suma sort", suma_sort)
    tablica = [[] for i in range(int(ilosc_maszyn))]
    tablica[0].insert(0,czasy_na_maszynach[0][tab_zadan[0]])
    tablica[1].insert(0,czasy_na_maszynach[1][tab_zadan[0]])
    tablica[2].insert(0,czasy_na_maszynach[2][tab_zadan[0]])
    cmax = suma_sort[0][0]
    for i in range(len(tab_zadan)-1):
        k = tab_zadan[i+1]
        for m in range(len(tablica[0])):
            for j in range(ilosc_maszyn):
                tablica[j].insert(m,czasy_na_maszynach[j][k])
            cmaxn = Cmax(tablica,ilosc_maszyn)
            print("cmxn 1 ", cmaxn, "dla kolejnosci: ", tablica)
            if m == 0:
                cmax = cmaxn
                tab_temp = przepisanie_wart(tablica)
            if cmaxn < cmax:
                cmax = cmaxn
                tab_temp = przepisanie_wart(tablica)
            for j in range(ilosc_maszyn):
                tablica[j].pop(m)
            if m == len(tablica[0])-1:
                for j in range(ilosc_maszyn):
                    tablica[j].insert(m+1,czasy_na_maszynach[j][k])
                cmaxn = Cmax(tablica,ilosc_maszyn)
                print("cmax ost", cmaxn, "dla kolejnosci: ", tablica)
                if cmaxn < cmax:
                    cmax = cmaxn
                    tab_temp = przepisanie_wart(tablica)
                tablica = przepisanie_wart(tab_temp)
        print("cmax",cmax, "dla tab", tablica)
    print("cmax OSTATECZNY", cmax)

            

lista, ilosc_z, ilosc_m = czytanie_z_pliku("ta000.txt")
Cmax(lista, ilosc_m)
Neh(lista,ilosc_m,ilosc_z)

tab, b = kolejnoscNeh([[1,4,2,3,1],[1,1,4,4,2],[3,2,3,1,3]],3,5)
print(tab)