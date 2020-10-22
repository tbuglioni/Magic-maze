class Heroes:
    """define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game"""

    def __init__(self):
        self.inventory = [False, False, False]

    def _motion_up(self, hero_localisation, path):
        """ move up to hero """
        temporary_position = hero_localisation.pop(0)
        test = temporary_position - 100
        if test in path:
            hero_localisation.append(test)
        else:
            hero_localisation.append(temporary_position)

    def _motion_down(self, hero_localisation, path):
        """ move down to hero """
        temporary_position = hero_localisation.pop(0)
        test = temporary_position + 100
        if test in path:
            hero_localisation.append(test)
        else:
            hero_localisation.append(temporary_position)

    def _motion_right(self, hero_localisation, path):
        """ move right to hero """
        temporary_position = hero_localisation.pop(0)
        test = temporary_position + 1
        if test in path:
            hero_localisation.append(test)
        else:
            hero_localisation.append(temporary_position)

    def _motion_left(self, hero_localisation, path):
        """ move left to hero """
        temporary_position = hero_localisation.pop(0)
        test = temporary_position - 1
        if test in path:
            hero_localisation.append(test)
        else:
            hero_localisation.append(temporary_position)

    def _choice_direction(self, hero_localisation, path, direction):
        """ choice where to move """
        if direction == "up":
            self._motion_up(hero_localisation, path)
        elif direction == "down":
            self._motion_down(hero_localisation, path)
        elif direction == "right":
            self._motion_right(hero_localisation, path)
        elif direction == "left":
            self._motion_left(hero_localisation, path)

    def motion(self, hero_localisation, path, direction):
        """ define how to move """
        self._choice_direction(hero_localisation, path, direction)

    def getstuff(self, stuff_errased):
        """ add given stuff into the inventory """
        if stuff_errased == "element 1 is take by hero":
            self.inventory[0] = True
        elif stuff_errased == "element 2 is take by hero":
            self.inventory[1] = True
        elif stuff_errased == "element 3 is take by hero":
            self.inventory[2] = True
        else:
            pass
