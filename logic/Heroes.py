from logic.ItemsLab import ItemsLab


class Heroes:
    """ define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game  """
    
    def __init__(self):
        self.loc = [414]
        self.inventory = [0,0,0]

    def motion_up(self,path):
        val = self.loc.pop(0)  # recup la valeur loc
        test = val + 100  # test la valeur pop
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def motion_down(self, path):
        val = self.loc.pop(0)  # recup la valeur loc
        test = val - 100  # test la valeur pop
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def motion_right(self, path):
        val = self.loc.pop(0)  # recup la valeur loc
        test = val + 1  # test la valeur pop
        if test in path:
            self.loc.append(test)
        else:
            self.loc.append(val)

    def motion_left(self, path):
        val = self.loc.pop(0) #recup la valeur loc
        test = val -1 #test la valeur pop
        if test in path:
            self.loc.append(test)
        else :
            self.loc.append(val)


        # renvoie la valeur pop



    def inmotion(self,path, where):
        """ define movement to the hero on the path only """
        key = where
        i = [0]
        if key == "up":
            i[0] = self.loc[0] + 100
            if i[0] in path:
                self.loc = list(i)
                key = 0
            else:
                pass
        elif key == "down":
            i[0] = self.loc[0] - 100
            if i[0] in path:
                self.loc = list(i)
                key = 0
            else:
                pass
        elif key == "right":
            i[0] = self.loc[0] + 1
            if i[0] in path:
                self.loc = list(i)
                key = 0
            else:
                pass
        elif key == "left":
            i[0] = self.loc[0] - 1
            if i[0] in path:
                self.loc = list(i)
                key = 0
            else:
                key = 0

        else:
            pass
    
    def getstuff(self,nb):
        """ add given stuff into the inventory """
        if nb == 1:
            self.inventory[0] = 1
        elif nb == 2:
            self.inventory[1] = 1
        elif nb == 3:
            self.inventory[1] = 1
        else:
            pass


labyrinth = ItemsLab() # new game with walls and spaces
perso = Heroes() # new heroe in labyrinth, at start point
labyrinth.randomstuff() # add 3 objects in a random location on labyrinth

print("voici la position du hero :", perso.loc)
perso.motion_left(labyrinth.path)
print("voici la position du hero :", perso.loc)