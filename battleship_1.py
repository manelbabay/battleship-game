# -----------------------------------------------------------------------------------------------------------------------------
#                                                     Importation de la bibliothÃ¨que Numpy
# -----------------------------------------------------------------------------------------------------------------------------
# Nous avons choisi d'importer Numpy pour pouvoir manipuler notre grille sous forme de matrice en y stockant nos bateaux.
# Mais aussi de pouvoir gÃ©nÃ©rer des nombres alÃ©atoires pour crÃ©er les bateaux de l'ordinateur

import numpy as np

# -----------------------------------------------------------------------------------------------------------------------------
#                                             PrÃ©sentation des diffÃ©rentes fonctions que l'on va utiliser
# -----------------------------------------------------------------------------------------------------------------------------


def initialiserGrille (): 
    # Comme son nom l'indique cette fonction va avoir pour but d'initialiser la grille de l'ordinateur. 
    # Pour cela l'on va crÃ©e une matrice 10x10 coresppondant Ã  la taille de notre grille et la remplir de zÃ©ro.
    A=np.zeros((10,10))
    return A

  
def afficherGrille(A):
    # Cette fonction prend en argument une matrice dont elle va faire un affichage graphique sous forme de grille
    print(" ",np.arange(1,11,1))      #affichage du nom des colonnes 
    for i in range(10):
        print(chr(65+i),"|",end=' ')  #affichage du nom des lignes 
        for j in range (10):
            if A[i,j]==10:
                print("*",end=' |')   #si c'est une case d'eau qui a Ã©tÃ© touchÃ© 
            elif -5<=A[i,j]<0:
                print("+",end=' |')   # si c'est une case d'un bateau qui a Ã©tÃ© touchÃ© 
            elif A[i,j]<=-10:
                print("x",end=' |')   # si c'est une case d'un bateau qui a Ã©tÃ© coulÃ©
            else:
                print(" ",end=' |')
        print(" ")




def placerBateaux(A, n):
    # Cette fonction prend en argument une matrice qui sera directement modifier en mÃ©moire et une taille de bateau et va chercher comment placer le bateau
    bateau_place = False     # Introduction d'un boolÃ©en permettant la sortie de la boucle qu'on initialise Ã  Faux 
    
    while bateau_place==False :  # RÃ©pÃ©ter jusqu'Ã  trouver une position valide
        i = np.random.randint(0, 10)    # Position de dÃ©part alÃ©atoire (ligne)
        j = np.random.randint(0, 10)    # Position de dÃ©part alÃ©atoire (colonne)
        p = np.random.randint(0, 2)     # Choix alÃ©atoire entre placement horizontal (0) et vertical (1)

        if p == 0:  # Placement horizontal
            # 1ere condition: VÃ©rifie que le bateau tient dans la grille (j + n <= 10) 
            # 2eme condition: pas d'autres bateaux sur les cases concernÃ©es avec le np.all pour Ã©viter le chevauchement 
            if j + n <= 10 and np.all(A[i, j:j + n] == 0):
                A[i, j:j + n] = n # Place le bateau en remplissant les cases avec sa taille, cela nous permet de savoir quelle bateau se trouve Ã  telle place
                bateau_place = True
            
        else:  # Placement vertical
            if i + n <= 10 and np.all(A[i:i + n, j] == 0): # De mÃªme
                A[i:i + n, j] = n
                bateau_place = True



def dejajoue(i, j, B):
    # Cette fonction prend en argument une ligne, une colonne et la matrice et va tester si la case en question a dÃ©jÃ  Ã©tÃ© jouÃ© par le joueur  
    if B[i, j] < 0 or B[i, j] == 10:  # Si la case a dÃ©jÃ  Ã©tÃ© touchÃ©e (bateau si inf Ã  0 ou eau si Ã©gal Ã  10)
        return True    #  La case a dÃ©jÃ  Ã©tÃ© jouÃ© donc la fonction retourne Vrai
    return False         #  La case n'a pas Ã©tÃ© jouÃ© donc retourne Faux



def jouer(B, i, j,Nbr_bateau_coule):
    # Cette fonction prend en argument une ligne, une colonne, la matrice et le nombre de bateaux coulÃ© 
    # Elle va avoir pour objectif de changer la valeur de la case suivant ce qu'elle contenait originellement et ainsi la marquer comme jouÃ© 
    # Comme c'est une matrice cela changera directement en mÃ©moire donc pas besoin de retourner la matrice 
    valeur_bateau = B[i, j]   # Notation pour faciliter la comprÃ©hension 
    if valeur_bateau != 0:  # Bateau touchÃ©
        print("TouchÃ© !")
        B[i, j] = -valeur_bateau     # Marquer la case comme jouÃ©e
        if not (valeur_bateau in B): # VÃ©rifier si le bateau est coulÃ© pour cela on va regarder dans toute la grille s'il y a quelque part valeur_bateau
            Nbr_bateau_coule+=1      # on incrÃ©mente le nombre de bateau coulÃ© 
            for k in range(10):
                for l in range(10):
                    if B[k,l]==-valeur_bateau: #on parcours toute la matrice et Ã  chaque fois qu'on a un case touchÃ©e qui a la meme valeur que moins la prÃ©cÃ©dente on la marque comme coulÃ©
                        B[k,l]=B[k,l]*10
            print("CoulÃ© !")
    else:
        print("Ã€ l'eau.")
        B[i, j] = 10  # Marquer l'eau
    return Nbr_bateau_coule #permet de mettre Ã  jour le nombre de bateaux coulÃ©s dans le programme principal


def debut():   #affichage en console du dÃ©but de la partie 
    print("              ------------------------------------------------")
    print("              - Bienvenue dans la Bataille Navale: version 1 -")
    print("              ------------------------------------------------\n")
    print("\nVous allez affronter un ordinateur, les rÃ¨gles sont les suivantes:\n")
    print("-  L'ordinateur a disposÃ© ces bateaux de faÃ§ons horizontales ou verticales sur l'ensemble de la grille")
    print("\n Ils sont au nombre de cinq dont: ")
    print("- 1 Porte-avion (5 cases)\n - 1 Croiseur (4 cases)\n - 1 Contre-torpilleurs (3 cases)\n - 1 Sous-marin (2 cases)\n - 1 Barque (1 case)\n \n")
    print("Ã€ la fin de la partie, votre taux de rÃ©ussite pour toucher un bateau sera affichÃ©.")
    print("\nVous Ãªtes maintenant prÃªt Ã   jouer, bonne chance ! \n")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                      Programme principal
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


GrilleOrdi=initialiserGrille ()

for i in range(1,6):  #on place tous les bateaux de l'ordinateur dans la matrice en incrÃ©mentant la taille via une boucle 
    placerBateaux(GrilleOrdi, i)
    
    
Nbr_bateau_coule=0
Nbr_de_coups=0

debut()
afficherGrille(GrilleOrdi)

while Nbr_bateau_coule!=5:
    print("Dans quelle case voulez vous jouez? ")
    i_lettre = input("Ligne : ")
    if len(i_lettre) != 1:     # Evite les erreurs du style B7 au lieux de B puis 7
        print("Erreur : Veuillez entrer un seul caractÃ¨re pour la ligne (entre A et J).")
        i_lettre = input("Ligne : ")    # On suppose que l'utilisateur Ã  la deuxiÃ¨me tentative ne se trompe pas...
    i=ord(i_lettre)-65
    j= int(input(("Colonne : ")))-1
    
    if 0 <= i < 10 and 0 <= j < 10 and dejajoue(i, j, GrilleOrdi)==False :
        Nbr_de_coups+=1
        Nbr_bateau_coule = jouer(GrilleOrdi, i, j,Nbr_bateau_coule)
        afficherGrille(GrilleOrdi)
    else:
        print("CoordonnÃ©es invalides ! Veuillez entrer des valeurs pour les lignes entre A et J et pour le colonnes entre 1 et 10.")
     
print("Bravo tu as enfin reussi en ",Nbr_de_coups," coups, ce qui te fais un pourcentage de rÃ©ussite de",15*100/Nbr_de_coups, "% !")

if Nbr_de_coups<=50:
    print("Impressionnant ! Tu peux relever un dÃ©fi encore plus corsÃ© avec une version supÃ©rieure.")
    print("Affronte l'ordinateur pour dÃ©couvrir ses bateaux avant qu'il ne dÃ©truise les tiens !")
else:
    print("Pas mal, mais avec un peu plus de pratique, tu amÃ©lioreras encore ta stratÃ©gie !")


    


    