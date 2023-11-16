print("Tere tulemast!".center(50))


kool=input("\tMis koolis sa õpid?: ").capitalize() #str kool



kursus=int(input("Mis kuursusel?: ")) #int kursus




print("Tere tulemast kooli "+kool.upper()+"!\nOle hea "+str(kursus) +"kuursuse õpilaseks!") #kool="TTHK"

print("Tere tulemast kooli", kool.lower(),"!\nOle hea",kursus,"kuursuse õpilaseks!") #kool=


print("Tere tulemast kooli {0}!\nOle hea {1}.kuursuse õpetajaks!".format(kool,kursus))#kool="Tthk"
print(type(kool))
print(type(kursus))
arv1=float(input("Arv 1: "))
arv2=float(input("Arv 2: "))
pritn("{0} + {1} = {2}".format(arv1,arv2,arv1+arv2)) #summa
pritn("{0} - {1} = {2}".format(arv1,arv2,arv1-arv2)) #lahutamine
pritn("{0} * {1} = {2}".format(arv1,arv2,arv1*arv2)) #korrutis
pritn("{0} / {1} = {2}".format(arv1,arv2,arv1/arv2)) #jagamine
pritn("{0} ** {1} = {2}".format(arv1,arv2,arv1**arv2)) #astendamine
pritn("{0} ja {1} = {2}".format(arv1,arv2,arv1%arv2)) #jagamisjääk