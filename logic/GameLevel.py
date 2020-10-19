class GameLevel:
    """ all position in the game, from a level(x).txt"""

    def __init__(self):
        self.all_position = []
        self.path = []
        self.wall = []
        self.gard_localisation = []
        self.hero_localisation = []
        self.exit_localisation = []
        self.actual_level = 1

    def initialisation_lvl(self, lvl=1):
        """ import from file the lvl, analyse it, add all elements in categories """
        def importation_level():
            with open("level/level{}.txt".format(lvl), "r") as level_choice:
                text = level_choice.read()
            self.actual_level = int(lvl)
            return text

        def analyse_level(text):
            element_as_list = []
            for elt in text:
                if elt in "0123456":
                    element_as_list.append(elt)
            print(element_as_list)
            print("analyse len", len(element_as_list))
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
            position_case = 1
            counter = 1
            for elt in list:
                if elt == "0":
                    self.wall.append(position_case)
                    if counter == 15:
                        position_case += 86
                        counter = 1
                    else:
                        position_case += 1
                        counter += 1

                elif elt == "1":
                    self.path.append(position_case)
                    if counter == 15:
                        position_case += 86
                        counter = 1
                    else:
                        position_case += 1
                        counter += 1

                elif elt == "2":
                    self.hero_localisation.append(position_case)
                    self.path.append(position_case)
                    if counter == 15:
                        position_case += 86
                        counter = 1
                    else:
                        position_case += 1
                        counter += 1

                elif elt == "3":
                    self.gard_localisation.append(position_case)
                    self.path.append(position_case)
                    if counter == 15:
                        position_case += 86
                        counter = 1
                    else:
                        position_case += 1
                        counter += 1

                elif elt == "4":
                    self.exit_localisation.append(position_case)
                    self.path.append(position_case)
                    if counter == 15:
                        position_case += 86
                        counter = 1
                    else:
                        position_case += 1
                        counter += 1

        a = importation_level()
        b = analyse_level(a)
        assign_element_in_categorie(b)

        identify_all_possible_position()

    def get_next_lvl(self):
        next_lvl = self.actual_level + 1
        if next_lvl == 6:
            next_lvl == 1
        else:
            pass
        return next_lvl
