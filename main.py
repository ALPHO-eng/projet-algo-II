from livre import ajouterLivre, aficher_livres, rechercherLivre , suprimer_ou_archiver
import utilisateur
def menu():
    print("1. Ajouter un livre")
    print("2. Chercher un livre")
    print("3. Supprimer un livre")
    print("4. Afficher les livres")
    print("5. Emprunter un livre")
    print("6. Retourner un livre")
    print("7. Afficher l'historique")
    print("8. Vérifier les retards")
    print("9. Ajouter un utilisateur")
    print("10. Supprimer un utilisateur")
    print("11. Lister tous les utilisateurs")
    print("12. Quitter le programme\n")
    choix = int(input("\tSélectionner une option : "))
    return choix

def main():
    while True:
        choix = menu()
        if choix == 1:
            livre.ajouterLivre()
        elif choix == 2:
            livre.rechercherLivre()
        elif choix == 3:
            livre.supprimerLivre()
        elif choix == 4:
            livre.afficherLivres()
        elif choix == 5:
            livre.emprunterLivre()
        elif choix == 6:
            livre.retournerLivre()
        elif choix == 7:
            livre.afficherHistorique()
        elif choix == 8:
            livre.verifierRetards()
        elif choix==12:
            break
        elif choix == 9:
            utilisateur.ajouterUtilisateur()
        elif choix == 10:
            utilisateur.supprimerUtilisateur()
        elif choix == 11:
            utilisateur.listerUtilisateurs()
        else:
            print("Veuillez choisir une option valide\n")

        
       

if __name__ == "__main__":
    main()


