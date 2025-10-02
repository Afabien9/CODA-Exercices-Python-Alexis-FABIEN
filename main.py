def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Bonjour Alexis")

def exercice3():
    print("bonjour")
    print("je m'apelle Alexis")
    print("je suis etudiant, mais")

def exercice4():
   an=2025-int(input("année de naissance "))
   print("j'ai environ", an, "ans")

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    elif choix == "2":
        exercice2()
    elif choix == "3":
        exercice3()
    elif choix == "4":
        exercice4()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()