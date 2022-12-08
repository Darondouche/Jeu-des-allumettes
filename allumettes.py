#CONSIGNES
#jeu des allumettes : 50 au départ
#chaque joueur en retire entre 1 et 6
#celui qui ôte la dernière gagne le jeu 

#création de la fonction qui retire au tas la pioche du joueur
def removeChoice (leftover, choicePlayer) : 

    #on vérifie que le choix est compris entre 1 et 6
    if not 1 <= choicePlayer <= 6:
        print("Le nombre d'allumettes à retirer doit être compris entre 1 et 6.")
        choicePlayer = int(input("Choose a number between 1 and 6: "))
        return removeChoice(leftover, choicePlayer)

    #on vérifie que le choix n'excède pas la pioche 
    if choicePlayer > leftover:
        print("Le nombre d'allumettes à retirer ne doit pas pas être strictement supérieur à la pioche.")
        choicePlayer = int(input("Choose a number between 1 and 6: "))
        return removeChoice(leftover, choicePlayer)
        
    #on actualise la pioche avec le choix du joueur 
    else:
        leftover = leftover - choicePlayer 

    return leftover

def eachTurn (remaining) :

    #tant que la pioche n'est pas nulle on continue à jouer 
    while remaining > 0 :

        #je récupère le choix utilisateur et je le convertis en nombre 
        choicePlayer1 = int(input("Player 1, choose a number between 1 and 6: "))

        #je lance la fonction à chaque tour
        remaining = removeChoice(remaining, choicePlayer1)
        print(remaining) 

        #je contrôle si le jeu est terminé 
        if remaining == 0 : 
            print("Player 1, you won !")
            return

        #je créé le tour du joueur 2 
        choicePlayer2 = int(input("Player 2, choose a number between 1 and 6: "))

        #je lance la fonction à chaque tour
        remaining = removeChoice(remaining, choicePlayer2)
        print(remaining) 

        #je contrôle si le jeu est terminé 
        if remaining == 0 : 
            print("Player 2, you won !")
            return


#appel de la fonction qui lance le jeu 
eachTurn(50)



