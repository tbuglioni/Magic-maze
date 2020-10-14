from logic.ItemsLab import ItemsLab


class Heroes:
    """ define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game  """
    
    def __init__(self):
        self.loc = [414]
        self.inventory = [0,0,0]

    def motion_up(self,path):
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
        test = val -1
        if test in path:
            self.loc.append(test)
        else :
            self.loc.append(val)


    def getstuff(self,nb):
        """ add given stuff into the inventory """
        if nb == 1:
            self.inventory[0] = 1
        elif nb == 2:
            self.inventory[1] = 1
        elif nb == 3:
            self.inventory[2] = 1
        else:
            pass


labyrinth = ItemsLab() # new game with walls and spaces
perso = Heroes() # new heroe in labyrinth, at start point
labyrinth.randomstuff() # add 3 objects in a random location on labyrinth

print("voici la position du hero :", perso.loc)
perso.motion_left(labyrinth.path)
print("voici la position du hero :", perso.loc)