n= int (input("Unesi prirodan broj"))
prva_cifra=n//1000
print(prva_cifra)
druga_cifra=(n//100)%10
print(druga_cifra)
treca_cifra=(n//10)%10
print(treca_cifra)
zadnja_cifra=n%10
print(zadnja_cifra)

if prva_cifra==zadnja_cifra:
    s=(druga_cifra*10+treca_cifra)*(druga_cifra*10+treca_cifra)
    print(s)
else:
     print(prva_cifra*prva_cifra+ druga_cifra*druga_cifra+ treca_cifra*treca_cifra + zadnja_cifra*zadnja_cifra)