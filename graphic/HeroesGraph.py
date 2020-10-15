
import pygame
pygame.init()

class HeroesGraph:
    def __init__(self):


# import perso:
mcgyver = pygame.image.load("../image/MacGyver.png")
mcgyver = pygame.transform.scale(mcgyver, (48, 48))
mcgyver.convert_alpha()


# perso inventory

#import stuff1:
aiguille = pygame.image.load("../image/aiguille.png")
aiguille = pygame.transform.scale(aiguille, (48, 48))
aiguille.convert_alpha()

#import stuff2:
ether = pygame.image.load("../image/ether.png")
ether = pygame.transform.scale(ether, (48, 48))
ether.convert_alpha()

#import stuff3:
tube_plastique = pygame.image.load("../image/tube_plastique.png")
tube_plastique = pygame.transform.scale(tube_plastique, (48, 48))
tube_plastique.convert_alpha()