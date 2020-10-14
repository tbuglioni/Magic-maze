import pygame
from logic.ItemsLab import ItemsLab
from logic.Heroes import Heroes

# -----------------------------------------------------------------------
pygame.init()

windows_surface = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Mc Gyver: escape")

#import "bloc" = wall:
bloc = pygame.image.load("image/bloc.png")
bloc = pygame.transform.scale(bloc, (48, 48))
bloc.convert()

#import floor:
floor = pygame.image.load("image/floor.png")
floor = pygame.transform.scale(floor, (48, 48))
floor.convert()

#import stuff1:
aiguille = pygame.image.load("image/aiguille.png")
aiguille = pygame.transform.scale(aiguille, (48, 48))
aiguille.convert_alpha()

#import stuff2:
ether = pygame.image.load("image/ether.png")
ether = pygame.transform.scale(ether, (48, 48))
ether.convert_alpha()

#import stuff3:
tube_plastique = pygame.image.load("image/tube_plastique.png")
tube_plastique = pygame.transform.scale(tube_plastique, (48, 48))
tube_plastique.convert_alpha()

# import gard:
gard = pygame.image.load("image/Gardien.png")
gard = pygame.transform.scale(gard, (48, 48))
gard.convert_alpha()

# import perso:
mcgyver = pygame.image.load("image/MacGyver.png")
mcgyver = pygame.transform.scale(mcgyver, (48, 48))
mcgyver.convert_alpha()
# -----------------------------------------------------------------------
# new instance:
labyrinth = ItemsLab() # new game with walls and spaces
perso = Heroes() # new heroe in labyrinth, at start point
labyrinth.randomstuff() # add 3 objects in a random location on labyrinth

# -----------------------------------------------------------------------
# list with all position of the lab :
i = 1
k = 1
structure = [] # the list start empty
while i < 16: # add 1 new ligne after 15 columns
    j = 1
    while j < 16: # add 15 columns
        structure.append(k)
        j += 1
        k += 1
    k += 85
    i +=1

# creat list with wall
wall_stone = []
for nbr in structure:
    if nbr in labyrinth.path:
        pass
    else:
        wall_stone.append(nbr)

# compare 2 list and show image
def draw_on_lab(list1, list2, objet, x=0, y=672):
    """ compare list1(all position) with a specific list(with some position),
    and add picture in the position """
    counter = 1
    for elt in list1:
        if elt in list2:
            print(elt)
            windows_surface.blit(objet, (x, y))
            counter += 1
            x += 48
            if counter == 16:
                counter =1
                x = 0
                y -= 48
            else:
                pass
        else:
            counter += 1
            x += 48
            if counter == 16:
                counter = 1
                x = 0
                y -= 48
            else:
                pass

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
black_color = (0, 0, 0)

# loop zone :
my_game = True
while my_game:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            my_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                perso.motion_up(labyrinth.path)
            elif event.key == pygame.K_DOWN:
                perso.motion_down(labyrinth.path)
            elif event.key == pygame.K_RIGHT:
                perso.motion_right(labyrinth.path)
            elif event.key == pygame.K_LEFT:
                perso.motion_left(labyrinth.path)
    labyrinth.errase_stuff(perso.loc)
    draw_on_lab(structure, labyrinth.path, floor)
    draw_on_lab(structure, wall_stone, bloc)
    draw_on_lab(structure, labyrinth.gard, gard)
    draw_on_lab(structure, labyrinth.stuff1, aiguille)
    draw_on_lab(structure, labyrinth.stuff2, ether)
    draw_on_lab(structure, labyrinth.stuff3, tube_plastique)
    draw_on_lab(structure, perso.loc, mcgyver)

    pygame.display.flip()




pygame.quit()