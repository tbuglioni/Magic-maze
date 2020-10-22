import pygame

pygame.init()


class ItemsLabGraph:
    """ all graphical element for the labyrinth """

    def __init__(self):
        self.surface_game = 0
        self.path_graph = 0
        self.wall_graph = 0
        self.gard_graph = 0
        self.exit_graph = 0
        self.stuff1_graph = 0
        self.stuff2_graph = 0
        self.stuff3_graph = 0

    def new_window(
        self,
    ):
        """ create the main surface of pygame """
        self.surface_game = pygame.display.set_mode((720, 720))
        pygame.display.set_caption("Mc Gyver: escape")

    def _import_wall(self):
        """ import wall picture """
        bloc = pygame.image.load("image/bloc.png")
        bloc = pygame.transform.scale(bloc, (48, 48))
        bloc.convert()
        self.wall_graph = bloc

    def _import_floor(self):
        """ import floor picture """
        floor = pygame.image.load("image/floor.png")
        floor = pygame.transform.scale(floor, (48, 48))
        floor.convert()
        self.path_graph = floor

    def _import_gard(self):
        """ import gard picture """
        gard = pygame.image.load("image/Gardien.png")
        gard = pygame.transform.scale(gard, (48, 48))
        gard.convert_alpha()
        self.gard_graph = gard

    def _import_stuff1(self):
        """ import stuff1 picture """
        needle = pygame.image.load("image/aiguille.png")
        needle = pygame.transform.scale(needle, (48, 48))
        needle.convert_alpha()
        self.stuff1_graph = needle

    def _import_stuff2(self):
        """ import stuff2 picture """
        ether = pygame.image.load("image/ether.png")
        ether = pygame.transform.scale(ether, (48, 48))
        ether.convert_alpha()
        self.stuff2_graph = ether

    def _import_stuff3(self):
        """ import stuff3 picture """
        pipe = pygame.image.load("image/tube_plastique.png")
        pipe = pygame.transform.scale(pipe, (48, 48))
        pipe.convert_alpha()
        self.stuff3_graph = pipe

    def _import_exit_localisation(self):
        """ import exit picture """
        exit_location = pygame.image.load("image/downstairs.png")
        exit_location = pygame.transform.scale(exit_location, (48, 48))
        exit_location.convert()
        self.exit_graph = exit_location

    def import_items(self):
        """ import all picture"""
        self._import_wall()
        self._import_floor()
        self._import_gard()
        self._import_stuff1()
        self._import_stuff2()
        self._import_stuff3()
        self._import_exit_localisation()

    def add_graph(self, all_position, specific_position, image_to_add):
        """compare all spécific list(hero, gard, etc)
        with the main list, if it's the same number, in both :
        graph the good picture at the selected place"""
        column = 1
        x_position_image = 0
        y_position_image = 0
        x_image_size = 48
        y_image_size = 48
        max_image_xy = 15

        for elt in all_position:
            if elt in specific_position:
                self.surface_game.blit(
                    image_to_add, (x_position_image, y_position_image)
                )
                column += 1
                x_position_image += x_image_size
                if column == (max_image_xy + 1):
                    column = 1
                    x_position_image = 0
                    y_position_image += y_image_size
                else:
                    pass
            else:
                column += 1
                x_position_image += x_image_size
                if column == (max_image_xy + 1):
                    column = 1
                    x_position_image = 0
                    y_position_image += y_image_size
                else:
                    pass
