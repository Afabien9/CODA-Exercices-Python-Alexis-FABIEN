def exercice23():
    note=int(input("Quelle est ta note ? "))
    if note>20:
        print("Validé")
        print("Note Max 20/20")
    elif note>=10:
        print("Validé")
    elif note <10:
        print("Non Validé")