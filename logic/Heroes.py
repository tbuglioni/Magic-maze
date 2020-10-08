class Heroes:
    """ define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game  """
    
    def __init__(self):
        self.loc = 414
        self.inventory = [0,0,0]
    
    def inmotion(self,path):
        """ define movement to the hero on the path only """
        key = input("clic: 'z'=up,'s'=down,'d'=right,'q'=left ")
        if key == "z":
            i = self.loc + 100
            if i in path:
                self.loc = i
            else:
                pass
        elif key == "s":
            i = self.loc - 100
            if i in path:
                self.loc = i
            else:
                pass
        elif key == "d":
            i = self.loc + 1
            if i in path:
                self.loc = i
            else:
                pass
        elif key == "q":
            i = self.loc - 1
            if i in path:
                self.loc = i
            else:
                pass
        else:
            print("you have to choose only between 'zsdq'")
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
        

