import pygame
pygame.init()

class ItemsLabGraph:
    def __init__(self):

windows_surface = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Mc Gyver: escape")

#import "bloc" = wall:
bloc = pygame.image.load("../image/bloc.png")
bloc = pygame.transform.scale(bloc, (48, 48))
bloc.convert()

#import floor:
floor = pygame.image.load("../image/floor.png")
floor = pygame.transform.scale(floor, (48, 48))
floor.convert()

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

# import gard:
gard = pygame.image.load("../image/Gardien.png")
gard = pygame.transform.scale(gard, (48, 48))
gard.convert_alpha()
