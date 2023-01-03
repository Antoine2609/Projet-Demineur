import pygame
from pygame.locals import QUIT

# Initialise screen
pygame.init()
longueur_fenetre = 800
largeur_fenetre = 600
screen = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))
pygame.display.set_caption('Démineur')

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
pygame.display.flip()

# Event loop
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    screen.blit(background, (0, 0))
    pygame.display.flip()