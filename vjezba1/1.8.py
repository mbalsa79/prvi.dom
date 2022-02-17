#Napisati kod koji učitava dva cijela broja m i n štampa poruku „x je djeljiv sa y” ili „x nije
#djeljiv sa y“. Npr. „15 je djeljiv sa 3“ ili „15 nije djeljiv sa 4“.

n= int (input("Unesi prvi prirodan broj"))
m= int (input("Unesi drugi prirodni broj"))

def djeljiv(a,b):
  
    if a%b==0:
       # print(a)
        print(a," jeste djeljiv sa ",b)
    else:
        #print(a)
        print (a,"  nije djeljiv sa ",b)

djeljiv(n,m)