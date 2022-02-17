
from configparser import Interpolation
from time import process_time_ns

#Napisati kod koji za datu godinu odreñuje da li je prestupna i štampa odgovarajuću
#poruku. 
def Prestupna_godina():
    n=int  (input("Unesi godinu"))
    if n%4==0:
     print("Godina jeste prestupna")
    else:
        print("Godina nije prestupna")

Prestupna_godina()