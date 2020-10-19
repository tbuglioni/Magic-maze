import random


class ItemsLab:
    """ creating labyrinth with walls, path, and 3 stuffs on random location"""
    def __init__(self):
        self.all_stuff = []
        self.stuff1_localisation = []
        self.stuff2_localisation = []
        self.stuff3_localisation = []

    def add_random_stuff(self, path, gard_localisation, hero_localisation, exit_localisation):
        """ put on the path 3 stuffs in random location """
        free_localisation = list(path)
        free_localisation.remove(gard_localisation[0])
        free_localisation.remove(hero_localisation[0])
        free_localisation.remove(exit_localisation[0])
        random.shuffle(free_localisation)

        self.all_stuff = free_localisation[:3]
        self.stuff1_localisation.append(free_localisation[0])
        self.stuff2_localisation.append(free_localisation[1])
        self.stuff3_localisation.append(free_localisation[2])
    
    def errase_stuff(self, hero_localisation):
        """ check if the hero si on the same location of a stuff,
        and errase it, on the map """
        if hero_localisation == self.stuff1_localisation:
            self.stuff1_localisation = [0]
            return "element 1 is take by hero"
        elif hero_localisation == self.stuff2_localisation:
            self.stuff2_localisation = [0]
            return "element 2 is take by hero"
        elif hero_localisation == self.stuff3_localisation:
            self.stuff3_localisation = [0]
            return "element 3 is take by hero"
        else:
            return "none element is take by hero"
