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
    print(chiffre1, "+" , chiffre2 , "=" , chiffre1+chiffre2)


def exercice6():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    print(chiffre1, "-" , chiffre2 , "=" , chiffre1-chiffre2)


def exercice7():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    print(chiffre1, "x" , chiffre2 , "=" , chiffre1*chiffre2) 


def exercice8():
    chiffre1=int(input("1er nombre: "))
    chiffre2=int(input("2ème nombre: "))
    print(chiffre1, "/" , chiffre2 , "=" , chiffre1/chiffre2)


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
    
def exercice21():
    nombre=int(input("donnez moi un nombre "))
    if nombre<0:
        print("Négatif")
    elif nombre>0:
        print("positif")
    elif nombre==0:
        print("nul")

def exercice22():
    age=int(input("quelle est ton âge ? "))
    if age>=18:
        print("Majeur")
    elif age <18:
        print("Mineur")
    
def exercice23():
    note=int(input("Quelle est ta note ? "))
    if note>20:
        print("Validé")
        print("Note Max 20/20")
    elif note>=10:
        print("Validé")
    elif note <10:
        print("Non Validé")

def exercice24():
    chiffre1=int(input("1er Chiffre "))
    chiffre2=int(input("2eme Chiffre "))
    print("Le nombre le grand est", max(chiffre1, chiffre2))

def exercice25():
    chiffre1=int(input("1er Chiffre "))
    chiffre2=int(input("2eme Chiffre "))
    if chiffre1 <=chiffre2:
        print("Ta suite est croissante")
    else:
        print("Ta suite n'est pas croissante")

def exercice26():
    nombre=int(input("Donne moi un nombre "))
    if nombre % 5 == 0:
        print("Divisible par 5")
    else:
        print("Non Divisible par 5")

def exercice27():
    age=int(input("quelle est ton âge ? "))
    if age>=18:
        print("Adult")
    elif 12<=age<=17:
        print("ado")
    elif age <12:
        print("Enfant")

def exercice28():
    temp=int(input("quelle est la température ? "))
    if temp>100:
        print("Vapeur")
    elif 0<=temp<=100:
        print("Eau Liquide")
    elif temp <0:
        print("Glace")

def exercice29():
    note=int(input("quelle est votre note ? "))
    if note>20:
        print("Trés bien")
        print("Note Max 20/20")
    elif 0<=note<=8:
        print("Recalé")
    elif 9<=note<=11:
        print("Passable")
    elif 12<=note<=16:
        print("Bien")
    elif 17<=note<=20:
        print("Trés Bien")

def exercice30():
    n=int(input("N+ ? "))
    for k in range(n):
        print(k+1)

def exercice31():
    depart=int(input("Quelle est le chiffre de départ pour votre décompte ? " ))
    for k in range(depart, 0, -1):
        print(k)


def exercice32():
    chiffre=int(input("Quelle chiffre souhaitez vous aditionner ? "))
    somme=0
    for k in range(1,chiffre+1):
        somme+=k
        print(somme-k, "+", k, "=", somme)

def exercice33():
    table=int(input("Choisir une table entre 1 et 10 "))
    for k in range(1, 10):
        print(table, "x", k, "=", table*k)


def exercice34():
    arrive=int(input("Quelle est le chiffre d'arrivé pour votre décompte ? " ))
    for k in range(0, arrive, 2):
        print(k+2)

def exercice35():
    carre=int(input("Donne moi un carré parfait N ? "))
    for k in range(1, carre):
        n=carre**2
    print(carre,"²", "=", n)

def exercice36():
    mot=(input("donne moi un mot "))
    fois=int(input("combien de fois tu veux repeté le mot ? "))
    for k in range(fois):
        print(mot)

def exercice37():
    n=int(input("Entrez le nombre de lignes : "))

    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

def exercice38():
    a=float(input("Choisir le 1er nombre "))
    symboles_autorises = ('+', '-', '*', '/')
    operateur=(input("Entrer un operateur (+, -, *, /) : "))
    b=float(input("Choisir le 2ème nombre "))
    if operateur in symboles_autorises :
        
        if operateur == '+':
            print(a, "+", b, "=", a + b)
        elif operateur == '-':
            print(a, "-", b, "=", a - b)
        elif operateur == '*':
            print(a, "*", b, "=", a * b)
        elif operateur == '/':
            print(a, "/", b, "=", a / b)

    else:
        print("symbole non autorisé veuillez choisir un opérateur valide. ")






        
    
    











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
    elif choix == "21":
        exercice21()
    elif choix == "22":
        exercice22()
    elif choix == "23":
        exercice23()
    elif choix == "24":
        exercice24()
    elif choix == "25":
        exercice25()
    elif choix == "26":
        exercice26()
    elif choix == "27":
        exercice27()
    elif choix == "28":
        exercice28()
    elif choix == "29":
        exercice29()
    elif choix == "30":
        exercice30()
    elif choix == "31":
        exercice31()
    elif choix == "32":
        exercice32()
    elif choix == "33":
        exercice33()
    elif choix == "34":
        exercice34()
    elif choix == "35":
        exercice35()
    elif choix == "36":
        exercice36()
    elif choix == "37":
        exercice37()
    elif choix == "38":
        exercice38()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()