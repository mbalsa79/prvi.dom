from re import X

#Date su dvije promjenljive x i y istog tipa. Napisati kod koji mijenja mjesta vrijednostima u
#promjenljivim x i y. Npr. ako je x = 5 i y = 10, poslije izvršavanja koda treba da bude x=10 i
#y=5. 

x,y= input("Unesi vrijednosi ").split()
c=x 
x=y
y=c
print("Vrijednost x je  ")
print(x)
print("Vrijednost y je  ")
print(y)