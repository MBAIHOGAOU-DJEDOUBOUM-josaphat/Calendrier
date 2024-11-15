def afficher_calendrier(nombre_de_jours, premier_jour):
    jours_semaine = ["LUN", "MAR", "MER", "JEU", "VEN", "SAM", "DIM"]
    
    # Ajuster le premier jour pour correspondre à l'indice (1 pour lundi, 7 pour dimanche)
    premier_jour -= 1 

    # Affichage des en-têtes des jours
    print(" ".join(jours_semaine))

    # Insérer des espaces pour les jours avant le début du mois
    calendrier = ["    "] * premier_jour  # 4 espaces pour chaque cellule vide

    # Ajouter les jours du mois avec un formatage constant
    for jour in range(1, nombre_de_jours + 1):
        calendrier.append(f"{jour:>2}  ")  # Deux caractères pour le jour + 2 espaces

    # Affichage du calendrier par semaine
    for i in range(0, len(calendrier), 7):
        print("".join(calendrier[i:i+7]))

# Exemple d'utilisation avec validation des entrées
while True:
    try:
        nombre_de_jours = int(input("Entrez le nombre de jours dans le mois (28, 30 ou 31) : "))
        if nombre_de_jours not in [28, 30, 31]:
            raise ValueError("Nombre de jours invalide. Veuillez entrer 28, 30 ou 31.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        premier_jour = int(input("Entrez le premier jour du mois (1 pour lundi, 7 pour dimanche) : "))
        if premier_jour < 1 or premier_jour > 7:
            raise ValueError("Jour invalide. Veuillez entrer un nombre entre 1 et 7.")
        break
    except ValueError as e:
        print(e)

afficher_calendrier(nombre_de_jours, premier_jour)
