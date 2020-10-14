class Heroes:
    """ define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game  """
    
    def __init__(self):
        self.loc = [414]
        self.inventory = [0,0,0]

    def motion_up(self,path):
        test = [self.loc[0] + 100]
        if test in path:
            self.loc = list(test)
        else:
            pass
    def motion_down(self, path):
        test = [self.loc[0] - 100]
        if test in path:
            self.loc = list(test)
        else:
            pass

    def motion_right(self, path):
        test = [self.loc[0] + 1]
        if test in path:
            self.loc = list(test)
        else:
            pass
    def motion_left(self, path):
        test = [self.loc[0] - 1]
        if test in path:
            self.loc = list(test)
        else:
            pass

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


