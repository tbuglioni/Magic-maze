import pygame

pygame.init()


class HeroesGraph:
    """all graphical element for the hero :
    his own picture, and the inventory"""

    def __init__(self):
        self.hero_graph = 0
        self.stuff1_graph = 0
        self.stuff2_graph = 0
        self.stuff3_graph = 0

    def _import_avatar(self):
        """ import hero picture """
        avatar = pygame.image.load("image/MacGyver.png")
        avatar = pygame.transform.scale(avatar, (48, 48))
        avatar.convert_alpha()
        self.hero_graph = avatar

    def _import_stuff1_inv(self):
        """ import stuff1 picture """
        needle = pygame.image.load("image/aiguille.png")
        needle = pygame.transform.scale(needle, (30, 30))
        needle.convert_alpha()
        self.stuff1_graph = needle

    def _import_stuff2_inv(self):
        """ import stuff2 picture """
        ether = pygame.image.load("image/ether.png")
        ether = pygame.transform.scale(ether, (30, 30))
        ether.convert_alpha()
        self.stuff2_graph = ether

    def _import_stuff3_inv(self):
        """ import stuff3 picture """
        pipe = pygame.image.load("image/tube_plastique.png")
        pipe = pygame.transform.scale(pipe, (30, 30))
        pipe.convert_alpha()
        self.stuff3_graph = pipe

    def import_hero(self):
        """ import all picture"""

        self._import_avatar()
        self._import_stuff1_inv()
        self._import_stuff2_inv()
        self._import_stuff3_inv()

    def built_inventory(self, surface, inventory):
        """ add graphical inventory on the surface of the game"""
        black_color = (0, 0, 0)
        pygame.draw.rect(surface, black_color, (0, 0, 90, 35))
        if inventory[0]:
            surface.blit(self.stuff1_graph, [0, 0])
        else:
            pass

        if inventory[1]:
            surface.blit(self.stuff2_graph, [30, 0])
        else:
            pass

        if inventory[2]:
            surface.blit(self.stuff3_graph, [60, 0])
        else:
            pass
