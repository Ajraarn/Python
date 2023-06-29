import random

def deviner_nombre_secret():
    nombre_secret = random.randint(1, 100)
    nombre_essais = 0
    devine = False

    print("Bienvenue ! Devinez le nombre secret entre 1 et 100.")

    while not devine:
        nombre_essais += 1
        guess = int(input("Entrez votre estimation : "))

        if guess == nombre_secret:
            devine = True
            print(f"Bravo ! Vous avez trouvé le nombre secret en {nombre_essais} essai(s).")
        elif guess < nombre_secret:
            print("Le nombre secret est plus grand.")
        else:
            print("Le nombre secret est plus petit.")

    print(f"Le nombre secret était : {nombre_secret}")
    print(f"Nombre total d'essais : {nombre_essais}")

deviner_nombre_secret()