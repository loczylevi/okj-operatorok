class Operatorok:
    def __init__(self,sor):
        elso,operator,masodik = sor.strip().split(" ")
        self.elso = int(elso)
        self.operator = operator
        self.masodik = int(masodik)

with open("kifejezesek.txt","r",encoding="latin2") as f:
    lista = [Operatorok(sor) for sor in f]
    

print(f"2.feladat: Kifejezések száma: {len(lista)}")

maradekos_osztas = len([sor for sor in lista if sor.operator == "mod"])

print(f"3.feladat: Kifejezések maradékos osztással: {maradekos_osztas}")
van_e = False
for sor in lista:
    if sor.elso % 10 == 0 and sor.masodik % 10 == 0:
        van_e = True
        break

if van_e:
    print("4.feladat: Van ilyen kifejezés!")
else:
    print("4.feladat: Nincs ilyen kifejezés!")
    
mod = len([sor for sor in lista if sor.operator == "mod"])
osztas = len([sor for sor in lista if sor.operator == "/"])
egesz = len([sor for sor in lista if sor.operator == "div"])
kiv = len([sor for sor in lista if sor.operator == "-"])
szor = len([sor for sor in lista if sor.operator == "*"])
ossz = len([sor for sor in lista if sor.operator == "+"])

print(f"""5.feladat: Statisztika
       mod -> {mod} db
         / -> {osztas} db
       div -> {egesz} db
         - -> {kiv} db
         * -> {szor} db
         + -> {ossz} db""")

def szamolo(a):
    a = a.split()
    try:
        if a[1] == "div":
            eredmeny = int(a[0]) // int(a[2])
        elif a[1] == "+":
            eredmeny = int(a[0]) + int(a[2])
        elif a[1] == "-":
            eredmeny = int(a[0]) - int(a[2])
        elif a[1] == "*":
            eredmeny = int(a[0]) * int(a[2])
        elif a[1] == "/":
            eredmeny = int(a[0]) / int(a[2])
            eredmeny = str(eredmeny).replace(".",",")
        elif a[1] == "mod":
            eredmeny = int(a[0]) % int(a[2])
        else:
            eredmeny = "Hibás operátor!"
    except ZeroDivisionError:                  # nagyob barokkos ༼ つ ◕_◕ ༽つ
        eredmeny = "Egyéb hiba!"
    except OverflowError:
        eredmeny = "Egyéb hiba!"
    return str(eredmeny)
        

while True:
    bekeres = input("7. feladat: Kérek egy kifejezést (pl.: 1 + 1): ")
    if bekeres == "vége":
        break
    else:
        meghivo = szamolo(bekeres)
        print(f"        {bekeres} = {meghivo}")
        
with open("eredmenyek.txt","w") as f2:
    for sor in lista:
        bekeres = str(sor.elso) + " " + sor.operator + " " + str(sor.masodik)
        f2.write(f"{sor.elso} {sor.operator} {sor.masodik} = {szamolo(bekeres)}\n")
