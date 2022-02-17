# Domino se igra pločicama pravougaonog oblika, takvim da se na svakoj pločici nalaze
#dvije oznake. Svaka oznaka sastoji se od određenog broja tačkica. Broj tačkica zavisi o
#veličini skupa domina. U skupu domina veličine N broj tačkica na jednoj pločici može biti
#bilo koji broj između 0 i N, uključivo. U jednom skupu ne postoje dvije pločice potpuno
#jednakih oznaka, bez obzira na redosljed oznaka na pločici. U potpunom skupu veličine N
#nalaze se sve moguće pločice sa oznakama 0 do N. Npr. potpuni skup domina veličine 2
#sadrži šest pločica sa sljedećim oznakama:
#Napišite program koji će odrediti ukupan broj tačkica na svim pločicama u potpunom
#skupu domina veličine N. Vaš program treba da učita jedan prirodan broj N (1 ≤ N ≤ 1000)
#– veličinu potpunog skupa domina. Program treba da štampa ukupan broj tačkica na svim
#pločicama u potpunom skupu domina veličine N.  

n= int(input("Unesi broj "))
a=[]
p=1
s=0
while p<=n:
    e=p*(p+1)/2 + p*(p+1)
    #print(e)
    a.append(e)
    p=p+1
    s=s+e

#print(a)
print(s)