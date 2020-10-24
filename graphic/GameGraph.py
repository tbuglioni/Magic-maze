import pygame

pygame.init()


class GameGraph:
    """
    import win/loose image and create visual lvl counter
    """

    def __init__(self):
        self.win_graph = 0
        self.loose_graph = 0

    def _import_win(self):
        """ import win picture """
        win_image = pygame.image.load("./image/win.png")
        win_image = pygame.transform.scale(win_image, (720, 720))
        win_image.convert()
        self.win_graph = win_image

    def _import_loose(self):
        """ import loose picture """
        loose_image = pygame.image.load("./image/loose.png")
        loose_image = pygame.transform.scale(loose_image, (720, 720))
        loose_image.convert()
        self.loose_graph = loose_image

    def import_game_graph(self):
        """ import image "win" and "loose" """
        self._import_win()
        self._import_loose()

    def show_actual_lvl(self, surface, actual_lvl):
        """ add visual lvl counter """
        black_color = (0, 0, 0)
        white_color = (255, 255, 255)
        pygame.draw.rect(surface, black_color, (0, 690, 40, 30))
        arial_font = pygame.font.SysFont("arial.ttf", 20)
        lvl_text = arial_font.render("lvl:{}".format(actual_lvl),
                                     False, white_color)
        surface.blit(lvl_text, [5, 695])
