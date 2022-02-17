godina= int (input("Unesi godinu"))
mjesec = int (input("Unesi mjesec"))

def Broj_dana_u_mjesecu(godina, mjesec):

 if mjesec==1 or mjesec==3 or mjesec==5 or mjesec==7 or mjesec==8 or mjesec==10 or mjesec==12:
     print (31)
 if mjesec==4 or mjesec==6 or mjesec==9 or mjesec==11:
     print(30)
 if godina%4==0 and mjesec==2:
        print(29)
 if godina%4!=0 and mjesec==2 :
     print(28)

Broj_dana_u_mjesecu(godina, mjesec) 