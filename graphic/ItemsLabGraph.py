import pygame
pygame.init()


class ItemsLabGraph:
    def __init__(self):
        """ all graphical element for the labyrinth : his own picture """
        self.surface_game = 0
        self.path_graph = 0
        self.wall_graph = 0
        self.gard_graph = 0
        self.exit_graph = 0
        self.stuff1_graph = 0
        self.stuff2_graph = 0
        self.stuff3_graph = 0

    def new_window(self):
        """ create the main surface of pygame """
        self.surface_game = pygame.display.set_mode((720, 720))
        pygame.display.set_caption("Mc Gyver: escape")

    def import_items(self):
        """ import all picture"""
        def import_wall():
            """ import wall picture """
            bloc = pygame.image.load("image/bloc.png")
            bloc = pygame.transform.scale(bloc, (48, 48))
            bloc.convert()
            self.wall_graph = bloc
        import_wall()

        def import_floor():
            """ import floor picture """
            floor = pygame.image.load("image/floor.png")
            floor = pygame.transform.scale(floor, (48, 48))
            floor.convert()
            self.path_graph = floor
        import_floor()

        def import_gard():
            """ import gard picture """
            gard = pygame.image.load("image/Gardien.png")
            gard = pygame.transform.scale(gard, (48, 48))
            gard.convert_alpha()
            self.gard_graph = gard
        import_gard()

        def import_stuff1():
            """ import stuff1 picture """
            needle = pygame.image.load("image/aiguille.png")
            needle = pygame.transform.scale(needle, (48, 48))
            needle.convert_alpha()
            self.stuff1_graph = needle
        import_stuff1()

        def import_stuff2():
            """ import stuff2 picture """
            ether = pygame.image.load("image/ether.png")
            ether = pygame.transform.scale(ether, (48, 48))
            ether.convert_alpha()
            self.stuff2_graph = ether
        import_stuff2()

        def import_stuff3():
            """ import stuff3 picture """
            pipe = pygame.image.load("image/tube_plastique.png")
            pipe = pygame.transform.scale(pipe, (48, 48))
            pipe.convert_alpha()
            self.stuff3_graph = pipe
        import_stuff3()

        def import_exit_localisation():
            """ import exit picture """
            exit_location = pygame.image.load("image/downstairs.png")
            exit_location = pygame.transform.scale(exit_location, (48, 48))
            exit_location.convert()
            self.exit_graph = exit_location
        import_exit_localisation()

    def add_graph(self, list1, list2, object_to_blit, x=0, y=0):
        """ compare all spécific list(hero, gard, etc) with the main list, if it's the same number, in both :
        graph the good picture at the selected place"""
        counter = 1
        for elt in list1:
            if elt in list2:
                self.surface_game.blit(object_to_blit, (x, y))
                counter += 1
                x += 48
                if counter == 16:
                    counter = 1
                    x = 0
                    y += 48
                else:
                    pass
            else:
                counter += 1
                x += 48
                if counter == 16:
                    counter = 1
                    x = 0
                    y += 48
                else:
                    pass
