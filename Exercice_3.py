def afficher_info(etudiant):
    # Affiche les informations de l'étudiant à l'écran
    print("Informations de l'étudiant :")
    print(f"Nom : {etudiant['nom']}")
    print(f"Age : {etudiant['age']}")
    print(f"Matière préférée : {etudiant['matiere_preferee']}")

# Création d'un dictionnaire pour stocker les informations de l'étudiant
etudiant = {
    'nom': 'Sebastien',
    'age': 36,
    'matiere_preferee': 'Mathématiques'
}

# Appel de la fonction pour afficher les informations de l'étudiant
afficher_info(etudiant)