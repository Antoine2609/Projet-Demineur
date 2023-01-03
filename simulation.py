# importation des bibliothèques et des modules indispensables
from random import randint
import pygame
from pygame.locals import QUIT

import class_case
import class_tableaudejeu

if __name__ == '__main__':
    # initialisation du jeu avec 10 lignes, 15 colonnes et 25 mines
    sim = class_tableaudejeu.TableauDeJeu(10, 15, 25)
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
        return 20 # 20 x 20 (400 cases)
    elif level == 'difficile':
        return 25 # 25 x 25 (625 cases)
    else:
        niveau()

def surface_nom_de_fenetre():
    pygame.display.set_caption('Démineur')
    # Fill background
    # dimensions de la surface du nom de la fenêtre
    width = 200
    height = 50 
    background = pygame.Surface((width, height))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Démineur", True, (255, 0, 0), (250, 250, 250))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (600, 0)) # début des coordonnées en haut à gauche
    pygame.display.flip()

def surface_tableau():
    # Fill background
    # dimensions de la surface du tableau de jeu
    width = height = 600
    plateau = pygame.Surface((width, height))
    plateau.fill((150,150,150))

    for i in range(nb_cases_cote):
        for j in range(nb_cases_cote): # on parcourt les 2 dimensions
            # appeler la méthode pour récupérer la Surface de la case (i, j)
            case_surface = surface_case(i, j)
            # poser la Surface de la case (i,j) sur la Surface du tableau de jeu
            # todo 

    # Blit everything to the screen
    screen.blit(plateau, (0, 0)) # début des coordonnées en haut à gauche
    pygame.display.flip()


def surface_case(i: int, j: int) -> pygame.Surface:
    case = sim.get_case(i, j)
    nom_fichier = ''
    if case.get_case_recouverte():
        if case.get_drapeau():
            nom_fichier = 'drapeau.png'
        else:
            nom_fichier = 'mystere.png'
    else:
        if case.get_mine():
            nom_fichier = 'mine.png'
        else:
            nb_mines = sim.nbr_mines_adjacentes_a_case()
            nom_fichier = '' + nb_mines + '.png'
    img = pygame.image.load(nom_fichier)
    img.convert()
    surface = pygame.Surface(img.get_rect())
    surface.blit(img, img.get_rect())
    return surface


# Initialise screen
pygame.init()
longueur_fenetre = 800
largeur_fenetre = 600
screen = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))

nb_cases_cote = niveau()

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            run = False

    surface_nom_de_fenetre()
    surface_tableau()
    pygame.display.flip()
    
'''
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