import pygame
from logic.ItemsLab import ItemsLab
from logic.Heroes import Heroes
from logic.GameLevel import GameLevel
from graphic.HeroesGraph import HeroesGraph
from graphic.ItemsLabGraph import ItemsLabGraph
pygame.init()


class Game:
    def __init__(self):
        self.boucle_statut = True
        self.new_game = GameLevel()
        self.perso = Heroes()
        self.show_perso = HeroesGraph()
        self.labyrinth = ItemsLab()
        self.show_items = ItemsLabGraph()

    def init_game(self, lvl):
        """ create new game : window, random items, add wall, gard, hero, start with lvl 1"""
        self.new_game.initialisation_lvl(lvl)
        self.show_items.new_window()
        self.show_items.import_items()
        self.show_perso.import_hero()
        self.labyrinth.add_random_stuff(self.new_game.path, self.new_game.gard_localisation,
                                        self.new_game.hero_localisation, self.new_game.exit_localisation)

    def interaction_game(self):
        """ items go from the map to the inventory"""
        self.perso.getstuff(self.labyrinth.errase_stuff(self.new_game.hero_localisation))

    def check_end(self):
        """ check if the game is over, and how ? win, loose ? and what to do after : restart, next-lvl ?"""
        def restart_game(game_lvl):
            """ all position of all items at origin position in the selected lvl file (file for each lvl)"""
            self.new_game.all_position = []
            self.new_game.path = []
            self.new_game.wall = []
            self.new_game.gard_localisation = []
            self.new_game.hero_localisation = []
            self.new_game.exit_localisation = []
            self.actual_level = game_lvl
            self.new_game.initialisation_lvl(game_lvl)
            self.labyrinth.stuff1_localisation = []
            self.labyrinth.stuff2_localisation = []
            self.labyrinth.stuff3_localisation = []
            self.perso.inventory = [False, False, False]
            self.labyrinth.add_random_stuff(self.new_game.path, self.new_game.gard_localisation,
                                            self.new_game.hero_localisation, self.new_game.exit_localisation)

        def kill_gard_or_loose():
            """ check the position of hero and inventory, if loose --> restart the game lvl1"""
            if (self.new_game.hero_localisation == self.new_game.gard_localisation) and \
                    (self.perso.inventory == [True, True, True]):
                self.new_game.gard_localisation = [0]
            elif (self.new_game.hero_localisation == self.new_game.gard_localisation) and \
                    (self.perso.inventory != [True, True, True]):
                restart_game(1)

            else:
                pass

        def win():
            """ check the final localisation if is == hero localisation --> start next lvl """
            if self.new_game.hero_localisation == self.new_game.exit_localisation:
                new_lvl = self.new_game.get_next_lvl()
                restart_game(new_lvl)

            else:
                pass  # it's note the ending location, the game continue
        kill_gard_or_loose()
        win()

    def all_event(self):
        """ loop with pygame event : quit, keyboard action"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.boucle_statut = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path, "up")
                elif event.key == pygame.K_DOWN:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path, "down")
                elif event.key == pygame.K_RIGHT:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path, "right")
                elif event.key == pygame.K_LEFT:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path, "left")

    def graph_all(self):
        """ compare all spécific list(hero, gard, etc) with the main list, if it's the same number, in both :
        graph the good picture at the selected place"""
        self.show_items.add_graph(self.new_game.all_position, self.new_game.path, self.show_items.path_graph)
        self.show_items.add_graph(self.new_game.all_position, self.new_game.wall, self.show_items.wall_graph)
        self.show_items.add_graph(self.new_game.all_position, self.new_game.gard_localisation,
                                  self.show_items.gard_graph)
        self.show_items.add_graph(self.new_game.all_position, self.new_game.exit_localisation,
                                  self.show_items.exit_graph)
        self.show_items.add_graph(self.new_game.all_position, self.labyrinth.stuff1_localisation,
                                  self.show_items.stuff1_graph)
        self.show_items.add_graph(self.new_game.all_position, self.labyrinth.stuff2_localisation,
                                  self.show_items.stuff2_graph)
        self.show_items.add_graph(self.new_game.all_position, self.labyrinth.stuff3_localisation,
                                  self.show_items.stuff3_graph)
        self.show_items.add_graph(self.new_game.all_position, self.new_game.hero_localisation,
                                  self.show_perso.hero_graph)
        self.show_perso.built_inventory(self.show_items.surface_game, self.perso.inventory)

    def refresh(self):
        """ actualise pygame window """
        pygame.display.flip()
