with open("kifejezesek.txt","r",encoding="latin2") as f:
    lista = [sor.strip().split() for sor in f]
    

print(f"2.feladat: Kifejezések száma: {len(lista)}")

maradekos_osztas = len([sor for sor in lista if sor[1] == "mod"])

print(f"3.feladat: Kifejezések maradékos osztással: {maradekos_osztas}")
van_e = False
for sor in lista:
    if int(sor[0]) % 10 == 0 and int(sor[2]) % 10 == 0:
        van_e = True
        break

if van_e:
    print("4.feladat: Van ilyen kifejezés!")
else:
    print("4.feladat: Nincs ilyen kifejezés!")
    
mod = len([sor for sor in lista if sor[1] == "mod"])
osztas = len([sor for sor in lista if sor[1] == "/"])
egesz = len([sor for sor in lista if sor[1] == "div"])
kiv = len([sor for sor in lista if sor[1] == "-"])
szor = len([sor for sor in lista if sor[1] == "*"])
ossz = len([sor for sor in lista if sor[1] == "+"])

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
        
with open("eredmenyek2.txt","w") as f2:
    for sor in lista:
        bekeres = str(sor[0]) + " " + sor[1] + " " + str(sor[2])
        f2.write(f"{sor[0]} {sor[1]} {sor[2]} = {szamolo(bekeres)}\n")
