from math import * # matemaatilised funktsioonid
from random import *


print("Tere tulemast!".center(50))


kool=input("\tMis koolis sa õpid?: ").capitalize() #str kool



kursus=int(input("\tMis kuursusel?: ")) #int kursus


print("Tere tulemast kooli "+kool.upper()+"!\nOle hea "+str(kursus)+" kuursuse õpilaseks!") #kool="TTHK"

print("Tere tulemast kooli",kool.lower(),"!\nOle hea",kursus,"kuursuse õpilaseks!") #kool=tthk


print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!".format(kool,kursus))#kool="Tthk"
print(type(kool))
print(type(kursus))




arv1=float(input("Arv 1: "))
arv2=float(input("Arv 2: "))
pritn("{0} + {1} = {2}".format(arv1,arv2,arv1+arv2)) #summa
pritn("{0} - {1} = {2}".format(arv1,arv2,arv1-arv2)) #lahutamine
pritn("{0} * {1} = {2}".format(arv1,arv2,arv1*arv2)) #korrutis
pritn("{0} / {1} = {2}".format(arv1,arv2,arv1/arv2)) #jagamine
pritn("{0} atmes {1} = {2}".format(arv1,arv2,arv1**arv2)) #astendamine
pritn("{0} ja {1} = {2}".format(arv1,arv2,arv1%arv2)) #jagamisjääk
pritn("{0} ja {1} jagamise täis osa {2}".format(arv1,arv2,arv1//arv2)) #summa

Tehe=input("Mida teha: ")
v=eval(str(arv1)+tehe+str(arv2))
print(v)


#1
print("Tere, maailm!".center(50))

nimi=input("teie nimi on?: ").capitalize() #nimi

print("Tere, mailm!, Tervitan sind {0}!".format(nimi))

vanus=int(input("Kui vana sa oled?"))

print("tere, maailm! Tervitan sind {0}! Sa oled {1} aastat vana.".format(nimi, vanus))





#2
vanus = 18 #type(vanus) -> int

eesnimi = "Jaak" #str

pikkus = 16.5 #float

kas_käib_koolis = True #bool



#3
kommide_arv=int(input("Laual olevate kommide arv: "))

print("Laua peal on {0}".format(kommide_arv))

mitu=int(input("Mitu kommi sa soovid süüa: "))

kommide_arv-=mitu

print("Nüüd laua peal on ",kommide_arv)



#4
C=float(input("Ümbermõõt: ")) #C=2*pi*r=pi*d

d=round(C/pi,2) #import math -> math.pi

print("Läbimõõt: {0}".format(round(d,2)))




#6
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except :
    print("Andmetüübi viga")





#7
a1=randint(1,10)
a2=randint(1,10)
a3=randint(1,10)
a4=randint(1,10)
a5=randint(1,10)
print("Arvude {0},{1},{2},{3} ja {4} aritmeetiline keskmine on {5}".format(a1,a2,a3,a4,a5,(a1+a2+a3+a4+a5)/5))




#8
print(" @..@ ")
print(" ---- ")
print(" \__/ ")
print("^^ "" ^^")



#9
a=randint(1,10)
b=randint(1,10)
c=randint(1,10)
P=a+b+c
print("a+b+c")



#10
sõbrad=int(input("kui palju sõbraid?: "))
hind=12.90
hind/=sõbrad
print("iga sõber maksab" ,hind)