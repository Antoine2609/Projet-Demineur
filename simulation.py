# importation des bibliothèques et des modules indispensables
from random import randint
import pygame
from pygame.locals import QUIT

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
    
    # création de la fenêtre
    
    # fenetre.fill((250,0,0)) # couleur de la fenêtre

    # smallfont = pygame.font.SysFont('Corbel',35)
    # text = smallfont.render('QUIT', True, (255,255,255))
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
    bombe1 = pygame.image.load("images/mine.bmp")
    bombe2 = pygame.image.load("images/mine2.bmp")

    colonne = 0
    ligne = 0

    for line in tab_jeu._tab:
        for case in line:
            if colonne >= nb_cases_cote:
                colonne = 0
                ligne += 1
            screen.blit(recouverte, (10 + colonne * 16, 40 + ligne * 16))
            colonne += 1
        

    # boutton = pygame.image.load("images/nonpassee.bmp")
    # screen.blit(boutton, (200,200))

    pygame.display.flip()

    run = True

    while run:

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
        
        # if boutton.get_rect().collidepoint(pygame.mouse.get_pos()):
        #     boutton = pygame.image.load("images/nonpassee.bmp")
        
        # print(boutton.get_rect().bottomleft)
        # print(pygame.mouse.get_pos())

        # for i in range(nb_cases_cote):
        #     for j in range(nb_cases_cote): # on parcourt les 2 dimensions
        #         pygame.draw.rect(nb_cases_cote, [255]*3, [i*nb_cases_cote, j*nb_cases_cote, nb_cases_cote, nb_cases_cote], 1)

        # pygame.draw.rect(screen,(170,170,170),[100,100,60,60])
        # screen.blit(text, (100,100))
        # screen.blit(boutton, (200,200))
        pygame.display.update()

        # screen.blit(background, (0, 0))
        # pygame.display.flip()


if __name__ == '__main__':
    main()








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