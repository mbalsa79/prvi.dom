from tokenize import Triple

#Napisati kod koji provjerava da li je zbir cifara datog trocifrenog broj dvocifren broj. 
n= int(input("Unesi broj"))

def dvocifren(a):
    prva_cifra=a//100
    druga_cifra=(a//10)%10
    zadnja_cifra=a%10
    s=prva_cifra+druga_cifra+zadnja_cifra
    if s>9 and s<100:
        return True
    else:
        return False

if dvocifren(n)== True:
    print("Jeste dovcifren")
else:
    print("Nije dvocifren")
