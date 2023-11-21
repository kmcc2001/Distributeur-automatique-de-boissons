cappu = 0.40
choco = 0.50
thé = 0.60

boisson = input("choisir la boisson : ")

if boisson == "cappu":
    print("0.40 euros svp")
    montant = float(input("introduisez votre monnaie: "))
    prix = 0.40
elif boisson == "choco":
    print("0.50 euros svp")
    montant = float(input("inserez vos pièces: "))
    prix = 0.50
elif boisson == "thé":
    print("0.60 euros svp")
    montant = float(input("inserez vos pièces: "))
    prix = 0.60
else:
    print("Boisson non disponible")
    montant = 0

montant *= 100
prix *= 100
compteur = 0
monnaie = montant - prix  # en centimes
ma_liste = [50, 20, 10]

if monnaie < 0:
    print("Montant insuffisant")

else:
    print("Monnaie à rendre : {:.2f} euros".format(monnaie / 100))

    for i in ma_liste:
        compteur = monnaie // i
        monnaie = monnaie % i
        print(compteur, "pièce(s) de", i, "centimes")
