import pygame
pygame.init()


class HeroesGraph:
    def __init__(self):
        self.hero_graph = 0
        self.stuff1_inv = 0
        self.stuff2_inv = 0
        self.stuff3_inv = 0

    def import_hero(self):
        def import_avatar():
            avatar = pygame.image.load("image/MacGyver.png")
            avatar = pygame.transform.scale(avatar, (48, 48))
            avatar.convert_alpha()
            self.hero_graph = avatar
        import_avatar()

        def import_stuff1_inv():
            needle = pygame.image.load("image/aiguille.png")
            needle = pygame.transform.scale(needle, (48, 48))
            needle.convert_alpha()
            self.stuff1_graph = needle
        import_stuff1_inv()

        def import_stuff2_inv():
            ether = pygame.image.load("image/ether.png")
            ether = pygame.transform.scale(ether, (48, 48))
            ether.convert_alpha()
            self.stuff2_graph = ether
        import_stuff2_inv()

        def import_stuff3_inv():
            pipe = pygame.image.load("image/tube_plastique.png")
            pipe = pygame.transform.scale(pipe, (48, 48))
            pipe.convert_alpha()
            self.stuff3_graph = pipe
        import_stuff3_inv()
