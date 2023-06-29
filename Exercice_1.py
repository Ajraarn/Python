def effectuer_operations():
    # Demander à l'utilisateur de saisir les deux nombres
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))

    # Calculer la somme des deux nombres
    somme = nombre1 + nombre2

    # Calculer la différence entre le premier nombre et le deuxième nombre
    difference = nombre1 - nombre2

    # Calculer le produit des deux nombres
    produit = nombre1 * nombre2

    # Vérifier si le deuxième nombre est différent de zéro avant de calculer le quotient
    if nombre2 != 0:
        quotient = nombre1 / nombre2
    else:
        quotient = "Division par zéro impossible"

    # Afficher les résultats des opérations
    print(f"Somme : {somme}")
    print(f"Différence : {difference}")
    print(f"Produit : {produit}")
    print(f"Quotient : {quotient}")

# Appeler la fonction pour exécuter les opérations
effectuer_operations()