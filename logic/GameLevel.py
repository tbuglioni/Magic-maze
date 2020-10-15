class GameLevel:
    """ class with all position of the game, from a level(x).txt"""

    def __init__(self):
        self.all_position = []
        self.path = []
        self.wall = []
        self.gard_localisation = []
        self.hero_localisation = []
        self.ending_column = [15, 115, 215, 215, 315, 415, 515, 615,
                              715, 815,915, 1015, 1115, 1215, 1315, 1415]
        self.actual_level = 1

    def initialisation_lvl(self, lvl):
        """ import from file the lvl, analyse it, add all elements in categories """
        def importation_level(lvl_nbr=1):
            with open("../level/level{}.txt".format(lvl_nbr), "r") as level_choice:
                text = level_choice.read()
            self.actual_level = lvl_nbr
            return text

        def analyse_level(text):
            element_as_list = []
            for elt in text:
                if elt in "0123":
                    element_as_list.append(int(elt))
            return element_as_list

        def assign_element_in_categorie(list):
            i = 1
            for elt in list:
                if elt == 1:
                    self.wall.append(i)
                    if i in self.ending_column:
                        i += 86
                    else:
                        i += 1
                elif elt == 0:
                    self.path.append(i)
                    if i in self.ending_column:
                        i += 86
                    else:
                        i += 1
                elif elt == 2:
                    self.hero_localisation.append(i)
                    if i in self.ending_column:
                        i += 86
                    else:
                        i += 1
                elif elt == 3:
                    self.gard_localisation.append(i)
                    if i in self.ending_column:
                        i += 86
                    else:
                        i += 1

        list_with_element = analyse_level(importation_level(lvl))
        assign_element_in_categorie(list_with_element)



perso = GameLevel()
perso.initialisation_lvl(1)
print(perso.path)
print(perso.gard_localisation)
