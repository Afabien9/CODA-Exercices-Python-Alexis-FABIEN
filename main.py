def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom=(input ("ton prenom "))
    print("Bonjour" , prenom)

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
    print(chiffre1, "+" , chiffre2 , "=" , chiffre1*chiffre2)


def exercice6():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    print(chiffre1, "x" , chiffre2 , "=" , chiffre1*chiffre2)


def exercice7():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    print(chiffre1, "x" , chiffre2 , "=" , chiffre1*chiffre2) 


def exercice8():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    print(chiffre1, "/" , chiffre2 , "=" , chiffre1*chiffre2)


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

def exercice12():
 for k in range(5):
    print("salut ")

def exercice13():
    for k in range(5):
        print(k+1)

def exercice14():
    for k in range(5):
        print("2 x " , k+1, "=", 2*(k+1))

def exercice15():
    perimetre=int(input("longueur des coté"))
    print("perimetre = ", (perimetre*4))

def exercice16():
    aire=int(input("longueur des coté"))
    print("aire = ", aire**2)

def exercice17():
    conversion=int(input("combien d'euro"))
    print(conversion, "€ =", conversion*1.1, "$")

def exercice18():
    minute=int(input("nombre de minutes "))
    print(minute, " minute =", minute*60, " seconde")

def exercice19():
    prixttc=int(input("combien d'euro "))
    print("prix TTC", prixttc*1.2, "€")

def exercice20():
    nom=(input("Votre Nom "))
    age=(input("Votre Âge "))
    print(nom, "a", age, "ans")
    






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
    elif choix == "12":
        exercice12()
    elif choix == "13":
        exercice13()
    elif choix == "14":
        exercice14() 
    elif choix == "15":
        exercice15() 
    elif choix == "16":
        exercice16()
    elif choix == "17":
        exercice17()
    elif choix == "18":
        exercice18()
    elif choix == "19":
        exercice19()
    elif choix == "20":
        exercice20()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()