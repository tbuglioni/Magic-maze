class Heroes:
    """ define interaction betwen mcgyver and items on the gride and
    the condition to the end of the game  """
    
    def __init__(self):
        self.inventory = [False,False,False]

    def motion(self, hero_localisation, path, direction):
        """ """

        def choice_direction():
            if direction == "up":
                motion_up()
            elif direction == "down":
                motion_down()
            elif direction == "right":
                motion_right()
            elif direction == "left":
                motion_left()

        def motion_up():
            temporary_position = hero_localisation.pop(0)
            test = temporary_position - 100
            if test in path:
                hero_localisation.append(test)
            else:
                hero_localisation.append(temporary_position)

        def motion_down():
            temporary_position = hero_localisation.pop(0)
            test = temporary_position + 100
            if test in path:
                hero_localisation.append(test)
            else:
                hero_localisation.append(temporary_position)

        def motion_right():
            temporary_position = hero_localisation.pop(0)
            test = temporary_position + 1
            if test in path:
                hero_localisation.append(test)
            else:
                hero_localisation.append(temporary_position)

        def motion_left():
            temporary_position = hero_localisation.pop(0)
            test = temporary_position -1
            if test in path:
                hero_localisation.append(test)
            else:
                hero_localisation.append(temporary_position)

        choice_direction()


    def getstuff(self,stuff_errased):
        """ add given stuff into the inventory """
        if stuff_errased == "element 1 is take by hero":
            self.inventory[0] = True
        elif stuff_errased == "element 2 is take by hero":
            self.inventory[1] = True
        elif stuff_errased == "element 3 is take by hero":
            self.inventory[2] = True
        else:
            pass