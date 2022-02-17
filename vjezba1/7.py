def void_manjiOdx(x):
    broj_ucitanih=0
    broj_parnih=0
    for i in range (0,x):

       broj_ucitanih=broj_ucitanih+1 
        
       if i%2==0:
         broj_parnih=broj_parnih+1
      
       

    
    print("Broj parnih brojeva je  ", broj_parnih)
    print("Broj ucitanih brojeva je ", broj_ucitanih)
    print("Zbir ucitanih brojeva je ", broj_ucitanih*(broj_ucitanih-1)/2)

x= int(input("Unesi broj: "))
void_manjiOdx(x)


