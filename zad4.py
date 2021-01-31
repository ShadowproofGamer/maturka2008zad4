import math
plik = open("dane.txt")
tab = []
wynik = [0,0,0,0,0,0]
wynik_ile = [0,0,0,0,0,0]
suma = []
plik2 = open("wybory", "w+")
for i in range(20):
    #print(i)
    temp = plik.readline().split()
    tab.append(temp)
#print(tab)

for i in range(20):
    temp = 0
    for j in range(6):
        wynik_ile[j] += int(tab[i][j])
        temp+=int(tab[i][j])
    suma.append(temp)

#ppt 4
for i in range(20):
    glosy = [0,0,0,0,0,0]
    for j in range(int(tab[i][6])):
        maks = int(tab[i][0])/(1+glosy[0])
        index = 0
        for k in range(1,6):
            temp = int(tab[i][k])/(1+glosy[k])
            if temp>maks:
                maks = temp
                index = k
        glosy[index]+=1
        wynik[index]+=1
    if i == 5:
        plik2.write("głosy w okręgu szóstym:"+"\n")
        print("głosy w okręgu szóstym:")
        plik2.write(" A: B: C: D: E: F:"+"\n")
        print(" A: B: C: D: E: F:")
        plik2.write(str(glosy)+"\n")
        print(glosy)
plik2.write("Komitety:"+"\n")
print("Komitety:")
plik2.write("Miejsca w parlamencie:"+"\n")
print("Miejsca w parlamencie:")
plik2.write(" A:  B:  C:  D:  E:  F:"+"\n")
print(" A:  B:  C:  D:  E:  F:")
plik2.write(str(wynik)+"\n")
print(wynik)
plik2.write("Komitety:"+"\n")
print("Komitety:")
plik2.write("oddane głosy na partie:"+"\n")
print("oddane głosy na partie:")
plik2.write(" A:    B:    C:    D:    E:    F:"+"\n")
print(" A:    B:    C:    D:    E:    F:")
plik2.write(str(wynik_ile)+"\n")
print(wynik_ile)
plik2.write("najmniej oddanych głosów w okręgu:"+"\n")
print("najmniej oddanych głosów w okręgu:")
plik2.write(str(suma.index(min(suma)))+"\n")
print(suma.index(min(suma)))
plik2.write("najwięcej oddanych głosów w okręgu:"+"\n")
print("najwięcej oddanych głosów w okręgu:")
plik2.write(str(suma.index(max(suma)))+"\n")
print(suma.index(max(suma)))
