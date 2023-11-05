import pygame
import random as rdm
from utils import *
import time


pygame.init()

# initialisation de l´écran avec sa taille et le titre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MY GAME")

# gestion de la vitesse de rafraichissement de l´écran
clock = pygame.time.Clock()

# dessiner un rectangle:
        # Créer un rectangle: rectangle= pygame.Rect(x,y,largeur,hauteur)
        # Le dessiner:        pygame.draw.rect(screen,couleur,rectangle)
        
# dessiner un cercle: pygame.draw.circle(screen,couleur, [x, y], rayon)

# ajouter du texte:
    #font1 = pygame.font.SysFont(None, 72)
    #txt1 = font1.render('NSI FOR EVER', True, GREY)

# ajouter une image:
    # vaisseau=pygame.image.load('JEU/vaisseau.png')

# Dessiner texte ou image dans la boucle du jeu:
    # texte: screen.blit(txt1,(x,y))
    # image: screen.blit(vaisseau,pygame.Rect(x,y,largeur,hauteur))

    

# creation des tirs
tirs=[]
def move_tirs():
    for tir in tirs:
        pygame.draw.rect(screen,BLACK,tir)
        tir.top-=5

run = True
# -------- Boucle principale du jeu -----------
while run:
    # fond d´écran
    screen.fill(WHITE)
    # --- Gestion des évènements
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("clic souris")
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print("Espace")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print("haut")
    if keys[pygame.K_DOWN]:
        print("bas")
    if keys[pygame.K_RIGHT]:
        print("droite")
    if keys[pygame.K_LEFT]:
        print("gauche")


    
    # Dessins





    # 60 mises à jour par seconde
    clock.tick(60)
    # mise à jour de l´écran
    pygame.display.update()

# On sort de la boucle et on quitte
pygame.quit()
 

