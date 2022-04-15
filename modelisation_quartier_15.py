## ☆ TIPE DE CHOC ☆ ##

## Modules importés (& scripts extérieurs ?) : Poulpie est super !

import numpy as np
import random as rd

## Squelette de notre matrice/quartier :

quartier = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,0],
                    [0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,2,0],
                    [0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0],
                    [0,2,2,2,0,2,2,2,0,2,2,2,2,0,2,2,2,0],
                    [0,2,2,2,0,2,2,2,0,2,2,2,2,0,2,2,2,0],
                    [0,2,2,2,0,2,2,2,0,0,0,2,2,0,2,2,2,0],
                    [0,2,2,2,0,0,0,0,0,0,0,2,2,0,2,2,2,0],
                    [0,2,2,2,2,2,2,2,0,2,0,2,2,0,2,2,2,0],
                    [0,2,2,2,2,2,2,2,0,2,0,0,0,0,0,2,2,0],
                    [0,0,0,0,2,2,2,2,0,2,0,0,0,0,0,2,2,0],
                    [0,2,2,0,2,2,2,2,0,2,2,2,0,2,0,0,0,0],
                    [0,2,2,0,2,2,2,2,0,2,2,2,0,2,0,0,0,0],
                    [0,2,2,0,0,0,0,0,0,0,2,2,0,2,2,2,2,0],
                    [0,2,2,2,2,2,2,2,2,0,2,2,0,2,2,2,2,0],
                    [0,2,2,2,2,2,2,2,2,0,2,2,0,2,2,2,2,0],
                    [0,2,2,2,2,2,2,2,2,0,0,0,0,0,2,2,2,0],
                    [0,2,2,2,2,2,2,2,2,2,2,0,2,0,2,2,2,0]])
#ATTENTION LES MATRICES N'ONT PAS DE VIRGULES

print(quartier[0]) #print une ligne
print(quartier.transpose()[0]) #print une colonne --> garder une matrice carrée
## Inventaire des croisements avec probabilités

inventaire_crois = {(0,0):(50,50),(0,8):(50,50),(0,17):(50,50),(3,0):(50,50),(3,4):(50,50),(3,8):(50,50),(3,13):(50,50),(3,17):(50,50),(7,4):(50,50),(7,8):(50,50),(7,10):(50,50),(10,0):(50,50),(10,3):(50,50),(10,10):(50,50),(10,13):(50,50),(10,14):(50,50),(12,14):(50,50),(12,17):(50,50),(13,3):(50,50),(13,9):(50,50),(16,9):(50,50),(16,12):(50,50),(16,13):(50,50)}
""" On définit le dictionnaire : {(tuple):(proba en %)} où le tuple (x1, x2) de proba est définit comme :
            x1 est proba qu'elle ne tourne pas et x2 = 1 - x1 """

## Programme du jour :

# La voiture qui tourne avec des probas : Done
# Eviter les voitures sur les croisements / collisions : Done
""" Imprimer la carte et la matricialiser :
    Les croisements à gérer à différents endroits / inventaire :
    Faire un programme qui fait passer toute une file de voiture (temps que ça prend selon les dispositions) :
    Lorsqu'on a le croisement à la fin de la matrice, peut-être essayer de garder la voiture (capturez-la !!!) :
    Gérer le module pygame (peut-être passer sur les ordinateurs perso) : """

## Les probabilités (& maths du coup) :

def proba(coord_crois) :
    """ On prend en argument les coordonnées d'un croisement et on renvoit la proba = {0,1} que la voiture tourne définit par :
            Si p = 1 : la voiture ne tourne pas (ie la voiture reste en L1)
            Si p = 0 : la voiture tourne (ie la voiture part en L2) """
    #proba_the = inventaire_crois[coord_crois]
    proba_theorique = (25,75) # En attendant d'avoir notre inventaire
    liste = [0,1]
    probabilité = rd.choices(liste, weights=(proba_theorique), k = 1)
    return probabilité[0]

## Scipts auxiliaires pour avancer :

def avancer(L1, b) :
    """ Fait avancer toutes la file et partir la dernière voiture
    b = {0,1} qui fait venir une dernière voiture """
    L = L1.copy()
    n = len(L)
    L[n-1] = 0
    for i in range(n-2,-1,-1) :
        if not(L[i+1]):
            L[i+1] = L[i]
            L[i] = 0
    if b :
        L[0] = 1
    return L

def avancer_fin(L,m) :
    """ Avancer la liste à partir de la position m incluse
    Rajoute un 0 à la position m """
    L1 = L.copy()
    L1 = L1[m:]
    L_f = avancer(L1,False)
    L_f = L[:m] + L_f
    return L_f

def avancer_debut(L,m,b) :
    """ Avancer la liste jusqu'à la position m (sans voiture)
    b = {0,1} qui fait venir une dernière voiture """
    assert(not(L[m]))
    L1 = L.copy()
    L1 = L1[:m+1]
    L_f = avancer(L1,b)
    L_f =  L_f + L[m+1:]
    return L_f

def avancer_debut_bloque(L,m,b) :
    """ Avancer toute la file de voiture jusqu'à la position m exclus
    La position m fait office de feu rouge (ie toutes les voitures d'avant avance si elles peuvent) """
    i = m-1
    while L[i]==1 :
        i-=1
        if i == 0 :
            return L
    return avancer_debut(L,i,b)


## Script d'un croisement :

def avancer_files(M1,M2,b1,b2,coord_crois) :

    """ Prend en argument une liste ligne (prioritaire) M1, une liste colonne M2, b1,b2, booléens pour savoir si une
    nouvelle voiture est insérée, et coord_croisement, tuple de deux coordonnées (indice ligne, indice colonne de la case croisement
    de la matrice --> voir modélisation du quartier) et qui fait avancer les deux files une seule fois """

    assert(len(M1)==len(M2))
    n = len(M1)
    L1 = M1.copy() #liste colonne
    L2 = M2.copy() #liste ligne
    x_m,y_m = coord_crois
    if L1[x_m] == 1 :
        L1[x_m] = proba(coord_crois)
        print("L1[x_m] :", L1[x_m])
        L2[y_m] = (1 - L1[x_m])
        print("L2[y_m] :", L2[y_m])
    L1_f = avancer_fin(L1,x_m)
    L2_f = avancer_fin(L2,y_m)
    if not(L1_f[x_m-1]) :
        L2_f = avancer_debut(L2_f,y_m,b2)
    else :
        L2_f = avancer_debut_bloque(L2_f,y_m,b2)
    L1_f = avancer_debut(L1_f,x_m,b1)
    return L1_f,L2_f


M1 = [1,0,1,1,0,1,1,2,0,0,0]
M2 = [1,0,1,1,1,0,0,0,1,0,0]

print(avancer_files(quartier[0],quartier.transpose()[0],0,0,(2,5)))













