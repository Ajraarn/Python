def gerer_liste_pays():
    # Créer une liste de pays initiale
    pays = ["France", "Allemagne", "Espagne", "Italie", "Japon"]
    
    # Afficher la liste de pays initiale
    print("Liste de pays initiale :", pays)

    # Ajouter le sixième pays "Canada" à la liste
    pays.append("Canada")
    print("Liste de pays après ajout du sixième pays :", pays)

    # Ajouter une nouvelle occurrence du troisième pays à la liste
    pays.append(pays[2])
    print("Liste de pays après ajout du troisième pays :", pays)

    # Remplacer le deuxième pays par "Australie"
    pays[1] = "Australie"
    print("Liste de pays après remplacement du deuxième pays :", pays)

    # Supprimer le quatrième pays de la liste
    del pays[3]
    print("Liste de pays après suppression du quatrième pays :", pays)

# Appeler la fonction pour exécuter les opérations sur la liste de pays
gerer_liste_pays()