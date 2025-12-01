import sys

classe = [
    ["Alice", 20, 15.5],
    ["Bob", 19, 12.0],
    ["Charlie", 22, 16.0]
]

def afficher_classe(classe):
    print("\n Liste des étudiants")
    if not classe:
        print("La classe est vide.")
        return
    for i, (nom, age, note) in enumerate(classe, start=1):
        print(f"{i}. {nom} | Age: {age} | Note: {note}")
    print("-" * 30)

def ajouter_etudiant(classe):
    print("\n Ajouter un étudiant")
    nom = input("Nom : ").strip()
    if not nom:
        print("Erreur: Le nom ne peut pas être vide.")
        return
    try:
        age = int(input("Âge : "))
        note = float(input("Note : "))
        classe.append([nom, age, note])
        print(f"Succès : {nom} a été ajouté.")
    except ValueError:
        print("Erreur : Saisie invalide (L'âge doit être entier, la note un chiffre).")

def supprimer_etudiant(classe):
    print("\n Supprimer un étudiant")
    afficher_classe(classe)
    if not classe:
        return
    try:
        choix = int(input("Numéro de l'étudiant à supprimer : "))
        etudiant_supprime = classe.pop(choix - 1)
        print(f"Succès : {etudiant_supprime[0]} a été supprimé.")
    except (ValueError, IndexError):
        print("Erreur : Numéro invalide.")

def mettre_a_jour_etudiant(classe):
    print("\n Modifier un étudiant")
    afficher_classe(classe)
    if not classe:
        return
    try:
        index = int(input("Numéro de l'étudiant à modifier : ")) - 1
        if index < 0 or index >= len(classe):
            print("Index hors limite.")
            return
        
        etudiant = classe[index]
        print(f"Modification de {etudiant[0]} (Appuie sur Entrée pour garder la valeur actuelle)")

        nouveau_nom = input(f"Nouveau nom ({etudiant[0]}) : ").strip()
        if nouveau_nom:
            etudiant[0] = nouveau_nom

        nouvel_age = input(f"Nouvel âge ({etudiant[1]}) : ").strip()
        if nouvel_age:
            try:
                etudiant[1] = int(nouvel_age)
            except ValueError:
                print("Âge invalide, valeur conservée.")

        nouvelle_note = input(f"Nouvelle note ({etudiant[2]}) : ").strip()
        if nouvelle_note:
            try:
                etudiant[2] = float(nouvelle_note)
            except ValueError:
                print("Note invalide, valeur conservée.")
        
        print("Mise à jour terminée.")

    except ValueError:
        print("Erreur : Saisie invalide.")

def afficher_statistiques(classe):
    print("\n Statistiques de la classe")
    if not classe:
        print("Pas assez de données.")
        return

    notes = [etudiant[2] for etudiant in classe]
    
    moyenne = sum(notes) / len(notes)
    meilleur = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])

    print(f"Nombre d'étudiants : {len(classe)}")
    print(f"Moyenne de la classe : {moyenne:.2f}/20")
    print(f"Meilleure note       : {meilleur[2]} ({meilleur[0]})")
    print(f"Moins bonne note     : {pire[2]} ({pire[0]})")

while True:
    print("\n GESTION DE CLASSE")
    print("1. Afficher tous les étudiants")
    print("2. Ajouter un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Modifier un étudiant")
    print("5. Statistiques")
    print("q. Quitter")

    choix = input("Votre choix : ").strip().lower()

    if choix == "1":
        afficher_classe(classe)
    elif choix == "2":
        ajouter_etudiant(classe)
    elif choix == "3":
        supprimer_etudiant(classe)
    elif choix == "4":
        mettre_a_jour_etudiant(classe)
    elif choix == "5":
        afficher_statistiques(classe)
    elif choix == 'q':
        print("Au revoir !")
        break
    else:
        print("Option inconnue, réessayez.")