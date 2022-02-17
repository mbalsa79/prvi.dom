from cgi import print_directory
import math
from xml.etree.ElementInclude import include

#Napisati kod koji za date katete a i b (a<b) pravouglog trougla računa površinu i
#zapreminu tijela koje se dobija rotacijom trougla oko manje katete
import math
a= int (input("Unesi duzinu manje katete"))
b= int (input("Unesi duzinu vece katete"))

def P_V_konusa(a,b):
 P=b*b*math.pi + b*math.pi*math.sqrt(a*a+b*b)
 V=b*b*math.pi*a/3
 print(P)
 print(V)

P_V_konusa(a,b)