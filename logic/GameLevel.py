class GameLevel:
    """ all position in the game, from a level(x).txt"""

    def __init__(self):
        self.all_position = []
        self.path = []
        self.wall = []
        self.gard_localisation = []
        self.hero_localisation = []
        self.exit_localisation = []
        self.ending_column = [15, 115, 215, 215, 315, 415, 515, 615,
                              715, 815,915, 1015, 1115, 1215, 1315, 1415]
        self.actual_level = 1

    def initialisation_lvl(self, lvl):
        """ import from file the lvl, analyse it, add all elements in categories """
        def importation_level(lvl):
            with open("../level/level{}.txt".format(lvl), "r") as level_choice:
                text = level_choice.read()
            self.actual_level = lvl
            return text

        def analyse_level(text):
            element_as_list = []
            for elt in text:
                if elt in "01234":
                    element_as_list.append(int(elt))
            return element_as_list

        def identify_all_possible_position():
            lign = 1
            index_number = 1
            while lign < 16:  # add 1 new lign after 15 columns
                column = 1
                while column < 16:  # add 15 columns
                    self.all_position.append(index_number)
                    column += 1
                    index_number += 1
                index_number += 85
                lign += 1

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
                elif elt == 4:
                    self.exit_localisation.append(i)
                    if i in self.ending_column:
                        i += 86
                    else:
                        i += 1

        list_with_element = analyse_level(importation_level(lvl))
        assign_element_in_categorie(list_with_element)
        identify_all_possible_position()

    def ending_game(self,inventory):
        def kill_gard_or_loose():
            if (self.hero_localisation == self.gard_localisation) and (inventory == [True, True, True]):
                self.gard_localisation = [0]
                return "gard is dead"
            elif (self.hero_localisation == self.gard_localisation) and (inventory != [True, True, True]):
                print("you lose, :/")
                return "loose"
            else:
                pass

        def win():
            if (self.hero_localisation == self.exit_localisation):
                return "win"
            else:
                pass  # it's note the ending location, the game continue

            kill_gard_or_loose()
            win()

    def get_next_lvl(self):
        next_lvl = self.actual_level += 1
        return next_lvl

new_game = GameLevel() #new instance game
new_game.initialisation_lvl(1) #initialise list
new_game.ending_game() #return "gard is dead" "loose" "win"
new_game.get_next_lvl() #return number