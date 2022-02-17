#Dat je cio broj k (1<=k<=180) i niz cifara 10111213...9899 koji se dobija kada se svi
#dvocifreni brojevi redom zapišu jedan iza drugog. Za dato k, odrediti dvocifreni broj koji
#sadrži k-tu cifru u datom nizu. Npr., za k=7, traženi broj je 13.

a=10
p=10
while a<99:
    p=p*100 +a+1
    a=a+1
k= int(input("Unesi k koje je se nalazi izmedju 1 i 180, ukljucujuci i te brojeve "))
if k%2==0:    
 q=p//(10**(180-k))
 if q>100:
     q=q%100
     print(q)
     exit()
 if q<100:
     print(q)
     exit()
if k%2!=0:
    q=p//(10**(180-k-1))
    if q<100:
     print(q)
     exit()
    if q>100:
        print(q%100)
        exit()
