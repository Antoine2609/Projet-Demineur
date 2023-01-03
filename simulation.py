# importation des bibliothèques et des modules indispensables
from random import randint
import pygame
from pygame.locals import QUIT
import math

import class_case
import class_tableaudejeu

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

def main():
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

    # nb_cases_cote = niveau()
    
    nb_cases_cote = 10
    tab_jeu = class_tableaudejeu.TableauDeJeu(nb_cases_cote, nb_cases_cote, 25)

    # Initialise screen
    pygame.init()
    largeur_fenetre = 16 * nb_cases_cote + 20
    hauteur_fenetre = 16 * nb_cases_cote + 60
    screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption('Jeu du démineur')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Démineur", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    
    # Blit everything to the screen
    screen.blit(background, (0, 0))

    recouverte = pygame.image.load("images/nonpassee.bmp")
    drapeau = pygame.image.load("images/drapeau.bmp")
    vide = pygame.image.load("images/rien.bmp")
    un = pygame.image.load("images/1.bmp")
    deux = pygame.image.load("images/2.bmp")
    trois = pygame.image.load("images/3.bmp")
    quatre = pygame.image.load("images/4.bmp")
    cinq = pygame.image.load("images/5.bmp")
    six = pygame.image.load("images/6.bmp")
    sept = pygame.image.load("images/7.bmp")
    huit = pygame.image.load("images/8.bmp")
    perdu = pygame.image.load("images/perdu.bmp")

    colonne = 0
    ligne = 0

    for line in tab_jeu._tab:
        for case in line:
            if colonne >= nb_cases_cote:
                colonne = 0
                ligne += 1
            screen.blit(recouverte, (10 + colonne * 16, 40 + ligne * 16))
            colonne += 1

    pygame.display.flip()

    run = True

    while run:

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                pos_x = mouse[0]
                pos_y = mouse[1]
                col = (pos_x - 10)//16
                lig = (pos_y - 40)//16

                case = tab_jeu.get_case(lig, col)

                if not case.get_drapeau() and case.get_case_recouverte():
                    tab_jeu.decouvrir_case(lig, col)
                    case = tab_jeu.get_case(lig, col)

                    if case.get_mine():
                        screen.blit(perdu, (10 + col * 16, 40 + lig * 16))
                        run = False
                        print('game over')
                    else:
                        n = tab_jeu.nbr_mines_adjacentes_a_case(lig, col)
                        if n == 0:
                            screen.blit(vide, (10 + col * 16, 40 + lig * 16))
                        elif n == 1:
                            screen.blit(un, (10 + col * 16, 40 + lig * 16))
                        elif n == 2:
                            screen.blit(deux, (10 + col * 16, 40 + lig * 16))
                        elif n == 3:
                            screen.blit(trois, (10 + col * 16, 40 + lig * 16))
                        elif n == 4:
                            screen.blit(quatre, (10 + col * 16, 40 + lig * 16))
                        elif n == 5:
                            screen.blit(cinq, (10 + col * 16, 40 + lig * 16))
                        elif n == 6:
                            screen.blit(six, (10 + col * 16, 40 + lig * 16))
                        elif n == 7:
                            screen.blit(sept, (10 + col * 16, 40 + lig * 16))
                        elif n == 8:
                            screen.blit(huit, (10 + col * 16, 40 + lig * 16))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                mouse = pygame.mouse.get_pos()
                pos_x = mouse[0]
                pos_y = mouse[1]
                col = (pos_x - 10)//16
                lig = (pos_y - 40)//16

                case = tab_jeu.get_case(lig, col)

                if case.get_drapeau():
                    screen.blit(recouverte, (10 + col * 16, 40 + lig * 16))
                else:
                    screen.blit(drapeau, (10 + col * 16, 40 + lig * 16))

                tab_jeu._tab[lig][col].set_drapeau()

        pygame.display.update()


if __name__ == '__main__':
    main()