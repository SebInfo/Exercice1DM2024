def afficher_menu():
    print("\nMenu :")
    print("1 : Ajouter une tâche")
    print("2 : Afficher les tâches")
    print("3 : Supprimer une tâche")
    print("4 : Quitter")

def ajouter_tache(taches):
    nom_tache = input("Entrez le nom de la tâche : ").strip()
    if nom_tache:
        taches.append(nom_tache)
        print(f"Tâche '{nom_tache}' ajoutée.")
    else:
        print("Le nom de la tâche ne peut pas être vide.")

def afficher_taches(taches):
    if not taches:
        print("Aucune tâche enregistrée.")
    else:
        print("\nListe des tâches :")
        for i, tache in enumerate(taches, start=1):
            print(f"{i}. {tache}")


def supprimer_tache(taches):
    afficher_taches(taches)
    if taches:
        try:
            numero = int(input("Entrez le numéro de la tâche à supprimer : "))
            if 1 <= numero <= len(taches):
                tache_supprimee = taches.pop(numero - 1)
                print(f"Tâche '{tache_supprimee}' supprimée.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


def main():
    taches = []
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ").strip()

        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            afficher_taches(taches)
        elif choix == "3":
            supprimer_tache(taches)
        elif choix == "4":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()