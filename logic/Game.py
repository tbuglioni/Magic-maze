import pygame
from logic.ItemsLab import ItemsLab
from logic.Heroes import Heroes
from logic.GameLevel import GameLevel
from graphic.HeroesGraph import HeroesGraph
from graphic.ItemsLabGraph import ItemsLabGraph
# ----------------------------------------------------------------------
# new instance:
new_game = GameLevel() #new instance game
new_game.initialisation_lvl(1) #initialise list
new_game.ending_game() #return "gard is dead" "loose" "win"
new_game.get_next_lvl() #return number


labyrinth = ItemsLab() # new game with walls and spaces
perso = Heroes() # new heroe in labyrinth, at start point
# add 3 objects in a random location on labyrinth
# ----------------------------------------------------------------------
class Game:
    def __init__(self):
        self.boucle_statut = True

    def new_instance(self):
        new_game = GameLevel()
        labyrinth = ItemsLab()
        perso = Heroes()
        show_perso = HeroesGraph()
        show_items = ItemsLabGraph()

    def check_end(self:):
        if new_game.ending_game(perso.inventory) == "loose":
            self.boucle_statut = False
        elif new_game.ending_game(perso.inventory) == "win":
            new_game.initialisation_lvl(new_game.get_next_lvl())




    def all_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.boucle_statut = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    perso.motion_up(labyrinth.path)
                elif event.key == pygame.K_DOWN:
                    perso.motion_down(labyrinth.path)
                elif event.key == pygame.K_RIGHT:
                    perso.motion_right(labyrinth.path)
                elif event.key == pygame.K_LEFT:
                    perso.motion_left(labyrinth.path)






# -----------------------------------------------------------------------
pygame.init()


# -----------------------------------------------------------------------


# -----------------------------------------------------------------------

# compare 2 list and show image
def draw_on_lab(list1, list2, objet, x=0, y=0):
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
                y += 48
            else:
                pass
        else:
            counter += 1
            x += 48
            if counter == 16:
                counter = 1
                x = 0
                y += 48
            else:
                pass

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


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
    analyse_case = labyrinth.errase_stuff(perso.loc)
    perso.getstuff(analyse_case)
    draw_on_lab(structure, labyrinth.path, floor)
    draw_on_lab(structure, wall_stone, bloc)
    draw_on_lab(structure, labyrinth.gard, gard)
    draw_on_lab(structure, labyrinth.stuff1, aiguille)
    draw_on_lab(structure, labyrinth.stuff2, ether)
    draw_on_lab(structure, labyrinth.stuff3, tube_plastique)
    draw_on_lab(structure, perso.loc, mcgyver)

    if (perso.loc == [1214]) and (perso.inventory == [True,True,True]):
        print("you win, congratulation :)") #ending location with invent : full
        print(perso.inventory)
        my_game = False # GOOD ending
    elif (perso.loc == [1214]) and (perso.inventory != [True,True,True]):
        print("you lose, :/ :)") #ending location with invent : not full
        print(perso.inventory)
        my_game = False # BAD ending
    else:
        pass # it's note the ending location, the game continue

    pygame.display.flip()




pygame.quit()