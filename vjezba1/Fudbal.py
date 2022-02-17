from xml.etree.ElementInclude import include
#Petar je posmatrao fudbalsku utakmicu i na papiru zapisivao rezultat sa
#semafora poslije svakog gola. Npr. mogući zapis je: 1:0, 1:1, 1:2, 2:2, 2:3. Zatim je Petar
#sabrao sve zapisane brojeve: 1+0+1+1+1+2+2+2+2+3=15. Na osnovu datog zbira,
# #napišite program koji određuje koliko je golova bilo na utakmici.

import math
N=int (input("Unesi zbir golova koje je Petar izracunao "))
def Fudbal(N):
 suma=(-1+ math.sqrt(1+8*N))/2
 print("Broj golova na ukamici je ",suma)

Fudbal(N)