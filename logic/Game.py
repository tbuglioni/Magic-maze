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
        self.new_game.initialisation_lvl(lvl)
        self.show_items.new_window()
        self.show_items.import_items()
        self.show_perso.import_hero()
        self.labyrinth.add_random_stuff(self.new_game.path, self.new_game.gard_localisation,
                                        self.new_game.hero_localisation, self.new_game.exit_localisation)

    def interaction_game(self):
        self.perso.getstuff(self.labyrinth.errase_stuff(self.new_game.hero_localisation))

    def check_end(self):
        def kill_gard_or_loose():
            if (self.new_game.hero_localisation == self.new_game.gard_localisation) and (self.perso.inventory == [True, True, True]):
                self.new_game.gard_localisation = [0]
                print("gard is dead")
            elif (self.new_game.hero_localisation == self.new_game.gard_localisation) and (self.perso.inventory != [True, True, True]):
                print("you lose, :/")
                self.boucle_statut = False

            else:
                pass

        def win():
            if self.new_game.hero_localisation == self.new_game.exit_localisation:
                new_lvl = self.new_game.get_next_lvl()
                print("vous gagnez")
                self.new_game.all_position = []
                self.new_game.path = []
                self.new_game.wall = []
                self.new_game.gard_localisation = []
                self.new_game.hero_localisation = []
                self.new_game.exit_localisation = []
                self.actual_level = new_lvl
                self.new_game.initialisation_lvl(new_lvl)
                self.labyrinth.stuff1_localisation = []
                self.labyrinth.stuff2_localisation = []
                self.labyrinth.stuff3_localisation = []
                self.perso.inventory = [False,False,False]
                self.labyrinth.add_random_stuff(self.new_game.path, self.new_game.gard_localisation,
                                                self.new_game.hero_localisation, self.new_game.exit_localisation)


            else:
                pass  # it's note the ending location, the game continue

        kill_gard_or_loose()
        win()


    def all_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.boucle_statut = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path,
                                      self.new_game.gard_localisation, self.new_game.exit_localisation, "up")
                elif event.key == pygame.K_DOWN:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path,
                                      self.new_game.gard_localisation, self.new_game.exit_localisation, "down")
                elif event.key == pygame.K_RIGHT:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path,
                                      self.new_game.gard_localisation, self.new_game.exit_localisation, "right")
                elif event.key == pygame.K_LEFT:
                    self.perso.motion(self.new_game.hero_localisation, self.new_game.path,
                                      self.new_game.gard_localisation, self.new_game.exit_localisation, "left")

    def graph_all(self):
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

    def refresh(self):
        pygame.display.flip()
