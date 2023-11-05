import random as rdm
import pygame

# Quelques couleurs...
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)


# Initialisation de la hauteur et la largeur de l´écran  
W = 700
H = 600
size = [W, H] 


class Sprite:
    def __init__(self,screen, img,x,y,largeur,hauteur,speed):
        self.image=pygame.image.load(img)
        self.screen=screen
        self.x=x
        self.y=y
        self.largeur=largeur
        self.hauteur=hauteur
        self.speed=speed
        
    def draw(self):
        self.screen.blit(self.image,pygame.Rect(self.x,self.y,self.largeur,self.hauteur))
        
    

        


 