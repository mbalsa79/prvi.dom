from turtle import end_fill

#Date su cifre dva broja: jednog trocifrenog (a3, a2 i a1) i jednog dvocifrenog (b2 i b1).
#Cifre a1 i b1 su cifre jedinica, cifre a2 i b2 su cifre desetica, a a3 je cifra stotina. Ako je
#poznato da je zbir ta dva broja trocifren broj, odrediti cifre zbira.

a1= int (input("Unesi cifru jedince trocifrenoga broja"))
a2=int (input("Unesi cifru desetice trocifrenoga broja"))
a3=int (input("Unesi cifru stotine trocifrenoga broja"))
b1=int (input("Unesi cirfu jedinca dvocifrenoga broja"))
b2=int (input("Unesi cifru desetice dvocifrenoga broja"))
#print(a1,a2,a3,b1,b2)
if a1+b1>10:
    C=(a1+b1)%10
    x=a2+b2+1
    if x>10:
        B=x%10
        A=a3+1
        print(A,B,C)
        exit()
    if x<10:
     B=x
    A=a3
    print(A,B,C) 
    exit()
if a1+b1<10:
    C=a1+b1
    p=a2+b2
    if p>10:
     B=p%10
     A=a3+1
     print(A,B,C)
     exit()
    if p<10:
        B=p
        A=a3
        print(A,B,C)
        exit()

