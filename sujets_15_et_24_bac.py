# Sujet n°15
# Exercice 1
def RechercheMinMax(tab):
    # fonction RechercheMinMax qui prend en paramètre un tableau de nombres non triés tab
    dict = {}
    if len(tab) > 1:
        mini = tab[0]
        maxi = tab[0]
        for min in tab:
            if tab[min] < mini:
                mini = tab[min]
        for max in tab: 
            if tab[max] > maxi:
                maxi = tab[maxi]
        dict['min'] = mini
        dict['max'] = maxi
    else:
        dict['min'] = None
        dict['max'] = None
    return dict # renvoie la plus petite et la plus grande valeur du tableau sous la forme d’un dictionnaire à deux clés ‘min’ et ‘max’

tableau1 = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1]
tableau2 = []
print(RechercheMinMax(tableau1))
print(RechercheMinMax(tableau2))

# Sujet n°24
# Exercice 1
def recherche(elt, tab):
    # fonction recherche qui prend en paramètres elt un nombre et tab un tableau de nombres
    indice = -1
    if elt in tab:
        for search in range(len(tab)):
            if tab[search] == elt:
                indice = search
    return indice # renvoie l’indice de la dernière occurrence de elt dans tab si elt est dans tab et le -1 sinon

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(1, [1, 50, 1]))
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))
