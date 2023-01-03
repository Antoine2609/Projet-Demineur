# démineur

# importation des bibliothèques et des modules indispensables
from random import randint
import pygame



########################################################################################################################################



class Case:
    def __init__(self):
        self._mine = False
        self._case_recouverte = True
        self._drapeau = False
    
    def get_mine(self) -> bool:
        return self._mine

    def set_mine(self):
        self._mine = True  

    def get_case_recouverte(self) -> bool:
        return self._case_recouverte
    
    def set_case_decouverte(self):
        '''
        méthode permettant de découvrir la case si elle ne possède pas de drapeau
        '''
        if not self._drapeau:
            self._case_recouverte = False

    def get_drapeau(self) -> bool:
        return self._drapeau

    def set_drapeau(self):
        '''
        méthode permettant d'inverser la valeur que prend le drapeau si la case n'est pas découverte
        '''
        if self.get_case_recouverte():
            self._drapeau = not self._drapeau




########################################################################################################################################



class TableauDeJeu:
    def __init__(self, lignes: int , colonnes: int, total_mines: int):
        self._dimensions_max = (lignes-1, colonnes-1)
        self._tab = [[Case() for _ in range(colonnes)] for _ in range(lignes)] # tableau à double dimension
        self._total_mines = total_mines # nombre de mines dans la matrice
        self.ajout_mines()
        self._cases_a_decouvrir = lignes * colonnes - total_mines

    def get_total_mines(self) -> int:
        return self._total_mines

    def get_dimensions(self) -> tuple:
        return self._dimensions_max

    def get_case(self, i: int, j: int) -> Case: 
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



########################################################################################################################################



if __name__ == '__main__':
    # initialisation du jeu avec 10 lignes, 15 colonnes et 25 mines
    sim = TableauDeJeu(10, 15, 25)
    # Toutes les coordonnées sont en base 0 (i.e. de 0 à (nb_lignes - 1))
    # Dans cet exemple, les lignes iront de 0 à 9, et les colonnes de 0 à 14
    # découverte d'une case aux coordonnées (5, 5)
    sim.decouvrir_case(5, 5)
    # nombre de mines autour de la case aux coordonnées (6, 1)
    sim.nbr_mines_adjacentes_a_case(6, 1)
    # positionnement d'un drapeau sur la case aux coordonnées (8, 11)
    sim.get_case(8, 11).get_drapeau()
    # état de la case aux coordonnées (6, 7) : recouverte ou découverte
    sim.get_case(6, 7).get_case_recouverte()
    # présence d'une mine ou non à la case aux coordonnées (2, 10)
    sim.get_case(2, 10).get_mine()
    # nombre de cases restant à découvrir
    sim.get_nb_cases_a_decouvrir()

    print('Démonstration terminée.')

def niveau():
    level = input("Choisissez votre niveau : facile, moyen ou difficile : ")
    if level == 'facile':
        return 10 # 10 x 10 (100 cases)
    elif level == 'moyen':
        return 15 # 15 x 15 (225 cases)
    elif level == 'difficile':
        return 20 # 20 x 20 (400 cases)
    else:
        niveau()

pygame.init()
# création de la fenêtre
longueur_fenetre = 800
largeur_fenetre = 600
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))
fenetre.fill((250,0,0)) # couleur de la fenêtre
pygame.display.set_caption("Jeu du démineur") # définition de la fenêtre

# création de la surface du tableau de jeu
width = height = 500
surface_plateau = pygame.surface((width, height), flags=0, depth=0, masks=None)
surface_plateau = pygame.Surface.fill((250,250,250)) # couleur de la surface

nb_cases_cote = niveau()

while run:
    
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            run = False

    for i in range(nb_cases_cote):
        for j in range(nb_cases_cote): # on parcourt les 2 dimensions
            pygame.draw.rect(surface_plateau, [255]*3, [i*nb_cases_cote, j*nb_cases_cote, nb_cases_cote, nb_cases_cote], 1)






'''
run = True

nb_cases_cote = niveau()

# min renvoie la valeur minimale d'une liste, ici la dimension de la fenêtre
taille_case = min(fenetre.get_size()) // nb_cases_cote - (min(fenetre.get_size()) // nb_cases_cote // nb_cases_cote)


while run:
    fenetre.fill((0,0,0)) # couleur de la fenêtre

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            run = False

    for x in range(nb_cases_cote):
        for y in range(nb_cases_cote): # on parcourt les 2 dimensions

            pygame.draw.rect(fenetre, [255]*3, [x*taille_case, y*taille_case, taille_case, taille_case], 1) # dessin du rect 

            lettre = font.render("?", True, [255]*3) # on crée la lettre
            lettre_rect = lettre.get_rect() # je recupere le rect
            lettre_rect.center = [x*taille_case + 1/2*taille_case, y*taille_case + 1/2*taille_case] # je place le centre du rect au milieu de la case
            fenetre.blit(lettre , lettre_rect ) # on blit le tout

    pygame.display.flip()

'''
'''
côté interface :
- temps
- graphique
- niveaux
- musique
- fond
- couleur
'''