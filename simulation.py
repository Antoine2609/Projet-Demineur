# importation des bibliothèques et des modules indispensables
from random import *
import pygame
from pygame.locals import *

import class_case
import class_tableaudejeu

def niveau():
    return 22
    '''
    level = input("Choisissez votre niveau : facile, moyen ou difficile : ")
    if level == 'facile':
        return 10 # 10 x 10 (100 cases)
    elif level == 'moyen':
        return 20 # 20 x 20 (400 cases)
    elif level == 'difficile':
        return 25 # 25 x 25 (625 cases)
    else:
        niveau()
    '''

def surface_nom_de_fenetre(screen):
    pygame.display.set_caption('Jeu du Démineur')
    # Fill background
    # dimensions de la surface du nom de la fenêtre
    width = 200
    height = 50 
    background = pygame.Surface((width, height))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Jeu du Démineur", True, (255, 0, 0), (250, 250, 250))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (550, 0)) # début des coordonnées en haut à gauche

def surface_tableau(screen, dimensions):
    # Fill background
    # dimensions de la surface du tableau de jeu
    width =  (dimensions[0] + 1) * 24
    height = (dimensions[1] + 1) * 24
    plateau = pygame.Surface((width, height))
    plateau.fill((150,150,150))

    for i in range(dimensions[0]+1):
        for j in range(dimensions[1]+1): # on parcourt les 2 dimensions
            # appeler la méthode pour récupérer la Surface de la case (i, j)
            case_surface = surface_case(i, j)
            # poser la Surface de la case (i,j) sur la Surface du tableau de jeu
            plateau.blit(case_surface, (i*24, j*24))
    screen.blit(plateau, (0, 0)) # début des coordonnées en haut à gauche



def surface_case(i: int, j: int) -> pygame.Surface:
    '''
    paramètres : coordonnées de la case
    retourne la surface de la case
    '''
    case = sim.get_case(i, j)
    nom_fichier = ''
    if case.get_case_recouverte():
        if case.get_drapeau():
            nom_fichier = 'drapeau.jpg'
        else:
            nom_fichier = 'couvert.jpg'
    else:
        if case.get_mine():
            nom_fichier = 'bombe.jpg'
        else:
            nb_mines = sim.nbr_mines_adjacentes_a_case(i, j)
            nom_fichier = str(nb_mines) + '.jpg'
    img = pygame.image.load(nom_fichier)
    img.convert()
    surface = pygame.Surface((img.get_rect().width, img.get_rect().height))
    surface.blit(img, img.get_rect())
    return surface


def mouse(event, sim : class_tableaudejeu.TableauDeJeu):
    if event.type == MOUSEBUTTONUP:
        position = event.pos
        button = event.button

        # coordonnées de la case sur laquelle on a cliqué
        i_tab = position[0] // 24
        j_tab = position[1] // 24
        
        if i_tab <= sim.get_dimensions()[0] and j_tab <= sim.get_dimensions()[1]: # vérifie si on est à l'intérieur de la zone de jeu
            # si boutton gauche : révélation d'une case
            if button == 1:
                sim.decouvrir_case(i_tab, j_tab)
            # si boutton droit : plantation d'un drapeau
            elif button == 3:
                sim.get_case(i_tab, j_tab).set_drapeau()


if __name__ == '__main__':
    # initialisation du jeu avec x lignes, x colonnes et x mines
    sim = class_tableaudejeu.TableauDeJeu(niveau(), niveau(), niveau()*niveau()//6)
    # Toutes les coordonnées sont en base 0 (i.e. de 0 à (nb_lignes - 1))
    # Dans cet exemple, les lignes iront de 0 à 9, et les colonnes de 0 à 14
    # découverte d'une case aux coordonnées (5, 5)
#    sim.decouvrir_case(5, 5)
    # nombre de mines autour de la case aux coordonnées (6, 1)
#    sim.nbr_mines_adjacentes_a_case(6, 1)
    # positionnement d'un drapeau sur la case aux coordonnées (8, 11)
#    sim.get_case(8, 11).get_drapeau()
    # état de la case aux coordonnées (6, 7) : recouverte ou découverte
#    sim.get_case(6, 7).get_case_recouverte()
    # présence d'une mine ou non à la case aux coordonnées (2, 10)
#    sim.get_case(2, 10).get_mine()
    # nombre de cases restant à découvrir
#    sim.get_nb_cases_a_decouvrir()

#    print('Démonstration terminée.')

    # Initialise screen
    pygame.init()
    longueur_fenetre = 800
    largeur_fenetre = 600
    screen = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))
    surface_nom_de_fenetre(screen)

    run = True
    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                run = False
            mouse(event, sim)

        surface_tableau(screen, sim.get_dimensions())
        pygame.display.flip()
    