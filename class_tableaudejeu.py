# importation des bibliothèques et des modules indispensables
from random import randint
import pygame
import class_case

# class TableauDeJeu du projet démineur
class TableauDeJeu:
    def __init__(self, lignes: int , colonnes: int, total_mines: int):
        self._dimensions_max = (lignes-1, colonnes-1)
        self._tab = [[class_case.Case() for _ in range(colonnes)] for _ in range(lignes)] # tableau à double dimension
        self._total_mines = total_mines # nombre de mines dans la matrice
        self.ajout_mines()
        self._cases_a_decouvrir = lignes * colonnes - total_mines

    def get_total_mines(self) -> int:
        return self._total_mines

    def get_dimensions(self) -> tuple:
        return self._dimensions_max

    def get_case(self, i: int, j: int) -> class_case.Case: 
        '''
        i, j : indices du coefficient de la matrice carte
        renvoie la case ayant pour coordonnées (i ; j)
        '''
        return self._tab[i][j]

    def ajout_mines(self):
        '''
        ajoute aléatoirement des mines dans la matrice
        '''
        mines_in_matrice = 0
        while self._total_mines > mines_in_matrice:
            i = randint(0, self._dimensions_max[0])
            j = randint(0, self._dimensions_max[1])
            if not self.get_case(i, j).get_mine():
                self.get_case(i, j).set_mine()
                mines_in_matrice += 1

    def nbr_mines_adjacentes_a_case(self, i: int, j: int) -> int:
        '''
        paramètres : coordonnées de la case
        retourne le nombre de mines adjacentes à cette case
        '''
        nbr_mines_adj = 0
        for x in range(max(0, i-1), min(self._dimensions_max[0], i+1)):
            for y in range(max(0, j-1), min(self._dimensions_max[1], j+1)): # gère les cas limites -> cases au bord
                if self.get_case(x, y).get_mine() == True:
                        nbr_mines_adj += 1
        return nbr_mines_adj        


    def decouvrir_case(self, i: int, j: int) -> int:
        '''
        paramètres : coordonnées de la case
        but : révéle cette case si pas de drapeau et révèle les cases non recouvertes si pas de mines adjacentes
        si pas de drapeau : retourne le nombre de mines adjacentes à cette case
        '''
        if not self.get_case(i, j).get_drapeau():
            self.get_case(i, j).set_case_decouverte()
            self._cases_a_decouvrir -= 1
            if self.nbr_mines_adjacentes_a_case(i, j) == 0: # si pas de mines autour de la case découverte
                for x in range(max(0, i-1), min(self._dimensions_max[0], i+1)):
                    for y in range(max(0, j-1), min(self._dimensions_max[1], j+1)): # gère les cas limites -> cases au bord
                        if self.get_case(x, y).get_case_recouverte():
                            self.decouvrir_case(x, y) # récurrence
            return self.nbr_mines_adjacentes_a_case(i, j)
        return -1 # si la case possède un drapeau

    def get_nb_cases_a_decouvrir(self):
        '''
        nombre de cases restant à découvrir sans déclencher une mine
        '''
        return self._cases_a_decouvrir

