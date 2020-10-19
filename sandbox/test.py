import pygame

import random


class ItemsLab:
    """ creating labyrinth with walls, path, and 3 stuffs on random location"""

    def __init__(self):
        self.path = [
            5, 10, 11,
            102, 103, 104, 105, 107, 108, 110, 111, 113, 114,
            202, 204, 205, 208, 210, 211, 212, 213, 214, 215,
            302, 303, 304, 305, 306, 307, 308, 310, 312,
            401, 402, 408, 409, 410, 412, 413, 414,
            501, 502, 503, 504, 505,
            602, 604, 605, 607, 609, 610, 611, 612, 613, 614,
            702, 703, 704, 705, 707, 709, 713,
            802, 804, 805, 807, 809, 811, 812, 813, 814,
            902, 903, 904, 905, 906, 907, 909, 911,
            1002, 1004, 1009, 1011, 1012, 1013, 1014, 1015,
            1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1111, 1114,
            1202, 1204, 1205, 1211, 1214,
            1302, 1303, 1304, 1305, 1307, 1308, 1309, 1310, 1311, 1314,
            1404, 1407, 1408, 1409, 1410
        ]
        self.gard = [1314]
        self.stuff = []
        self.stuff1 = []
        self.stuff2 = []
        self.stuff3 = []

    def randomstuff(self):
        """ put on the path 3 stuffs in random location """
        freelocation = list(self.path)
        random.shuffle(freelocation)
        self.stuff = freelocation[:3]
        self.stuff1.append(freelocation[0])
        self.stuff2.append(freelocation[1])
        self.stuff3.append(freelocation[2])

    def errase_stuff(self, nb):
        """ check if the hero si on the same location of a stuff,
        and errase it, on the map """
        if nb == self.stuff1:
            self.stuff1 = [0]
            return 1
        elif nb == self.stuff2:
            self.stuff2 = [0]
            return 2
        elif nb == self.stuff3:
            self.stuff3 = [0]
            return 3
        else:
            return 4


class Heroes:
    """ define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game  """

    def __init__(self):
        self.loc = [414]
        self.inventory = [0, 0, 0]

    def motion_up(self, path):
        val = self.loc.pop(0)
        test = val + 100
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def motion_down(self, path):
        val = self.loc.pop(0)
        test = val - 100
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def motion_right(self, path):
        val = self.loc.pop(0)
        test = val + 1
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def motion_left(self, path):
        val = self.loc.pop(0)
        test = val - 1
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def getstuff(self, nb):
        """ add given stuff into the inventory """
        if nb == 1:
            self.inventory[0] = 1
        elif nb == 2:
            self.inventory[1] = 1
        elif nb == 3:
            self.inventory[2] = 1
        else:
            pass
# -----------------------------------------------------------------------
pygame.init()

windows_surface = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Mc Gyver: escape")


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

    if (perso.loc == [1214]) and (perso.inventory == [1,1,1]):
        print("you win, congratulation :)") #ending location with invent : full
        print(perso.inventory)
        return "win"
    elif (perso.loc == [1214]) and (perso.inventory != [1,1,1]):
        print("you lose, :/ :)") #ending location with invent : not full
        print(perso.inventory)
        return "loose"
    else:
        pass # it's note the ending location, the game continue

    pygame.display.flip()




pygame.quit()


def assign_element_in_categorie(list):
    i = 1401
    for elt in list:
        if elt == 0:
            self.wall.append(i)
            if i in self.ending_column:
                i -= 114
            else:
                i += 1
        elif elt == 1:
            self.path.append(i)
            if i in self.ending_column:
                i -= 114
            else:
                i += 1
        elif elt == 2:
            self.hero_localisation.append(i)
            if i in self.ending_column:
                i -= 114
            else:
                i += 1
        elif elt == 3:
            self.gard_localisation.append(i)
            if i in self.ending_column:
                i -= 114
        elif elt == 4:
            self.exit_localisation.append(i)
            if i in self.ending_column:
                i -= 114
            else:
                i += 1