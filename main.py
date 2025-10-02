def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Bonjour Alexis")

def exercice3():
    print("bonjour")
    print("je m'apelle Alexis")
    print("je suis etudiant")

def exercice4():
   an=2025-int(input("année de naissance "))
   print("j'ai environ", an, "ans")

def exercice5():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    addition=(chiffre1)+(chiffre2) 

    print ("le resultat est", addition)

def exercice6():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    soustraction=(chiffre1)-(chiffre2) 

    print ("le resultat est", soustraction)

def exercice7():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    multiplication=(chiffre1)*(chiffre2) 

    print ("le resultat est", multiplication)

def exercice8():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    division=(chiffre1)/(chiffre2) 

    print ("le resultat est", division)

def exercice9():
    chiffre=int(input("chiffre: "))
    aucarre=(chiffre)**2

    print ("le resultat est", aucarre)

def exercice10():
    chiffre=int(input("chiffre: "))
    double=(chiffre)*2

    print ("le resultat est", double)

def exercice11():
    chiffre=int(input("chiffre: "))
    moitie=(chiffre)/2

    print ("le resultat est", moitie)





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
    elif choix == "5":
        exercice5()
    elif choix == "6":
        exercice6()
    elif choix == "7":
        exercice7()
    elif choix == "8":
        exercice8()
    elif choix == "9":
        exercice9()
    elif choix == "10":
        exercice10()
    elif choix == "11":
        exercice11()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()