import pygame
import time
from logic.ItemsLab import ItemsLab
from logic.Heroes import Heroes
from logic.GameLevel import GameLevel
from graphic.HeroesGraph import HeroesGraph
from graphic.ItemsLabGraph import ItemsLabGraph
from graphic.GameGraph import GameGraph

pygame.init()


class Game:
    """
    link between all logic and graphic class
    use all class to create the game
    """

    def __init__(self):
        self.boucle_statut = True
        self._new_game = GameLevel()
        self._show_new_game = GameGraph()
        self._perso = Heroes()
        self._show_perso = HeroesGraph()
        self._labyrinth = ItemsLab()
        self._show_items = ItemsLabGraph()

    @property
    def new_game(self):
        return self._new_game

    @property
    def perso(self):
        return self._perso

    @property
    def show_perso(self):
        return self._show_perso

    @property
    def labyrinth(self):
        return self._labyrinth

    @property
    def show_items(self):
        return self._show_items

    @property
    def show_new_game(self):
        return self._show_new_game

    def init_game(self, lvl):
        """create new game : window, random items,
        add wall, gard, hero, start with lvl 1"""
        self.new_game.initialisation_lvl(lvl)
        self.show_items.new_window()
        self.show_items.import_items()
        self.show_perso.import_hero()
        self._show_new_game.import_game_graph()
        self.labyrinth.add_random_stuff(
            self.new_game.path,
            self.new_game.gard_localisation,
            self.new_game.hero_localisation,
            self.new_game.exit_localisation,
        )

    def interaction_game(self):
        """ items go from the map to the inventory"""
        self.perso.getstuff(
            self.labyrinth.errase_stuff(self.new_game.hero_localisation)
        )

    def _restart_game(self, game_lvl):
        """all position of all items at origin position
        in the selected lvl file (file for each lvl)"""
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
        self.labyrinth.add_random_stuff(
            self.new_game.path,
            self.new_game.gard_localisation,
            self.new_game.hero_localisation,
            self.new_game.exit_localisation,
        )

    def _kill_gard_or_loose(self):
        """check the position of hero and inventory,
        if loose --> restart the game lvl1"""
        if (self.new_game.hero_localisation
            == self.new_game.gard_localisation) and (
            self.perso.inventory == [True, True, True]
        ):
            self.new_game.gard_localisation = [0]
        elif (self.new_game.hero_localisation
              == self.new_game.gard_localisation) and (
            self.perso.inventory != [True, True, True]
        ):
            self.show_items.surface_game.blit(
                self.show_new_game.loose_graph, [0, 0])
            self.refresh()
            time.sleep(2)
            self._restart_game(1)
        else:
            pass

    def _win(self):
        """check the final localisation
        if is == hero localisation --> start next lvl"""
        if self.new_game.hero_localisation == self.new_game.exit_localisation:
            new_lvl = self.new_game.get_next_lvl()
            if self.new_game.actual_level == self.new_game.max_level:
                self.show_items.surface_game.blit(
                    self.show_new_game.win_graph, [0, 0]
                )  # position angle haut gauche
                self.refresh()
                time.sleep(2)
            else:
                pass
            self._restart_game(new_lvl)
        else:
            pass  # it's note the ending location, the game continue

    def check_end(self):
        """check if the game is over, and how ? win, loose ?
        and what to do after : restart, next-lvl ?"""
        self._kill_gard_or_loose()
        self._win()

    def all_event(self):
        """ loop with pygame event : quit, keyboard action"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.boucle_statut = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.perso.motion(
                        self.new_game.hero_localisation,
                        self.new_game.path, "up"
                    )
                elif event.key == pygame.K_DOWN:
                    self.perso.motion(
                        self.new_game.hero_localisation,
                        self.new_game.path, "down"
                    )
                elif event.key == pygame.K_RIGHT:
                    self.perso.motion(
                        self.new_game.hero_localisation,
                        self.new_game.path, "right"
                    )
                elif event.key == pygame.K_LEFT:
                    self.perso.motion(
                        self.new_game.hero_localisation,
                        self.new_game.path, "left"
                    )

    def graph_all(self):
        """compare all spécific list(hero, gard, etc)
        with the main list, if it's the same number, in both :
        graph the good picture at the selected place"""
        self.show_items.add_graph(
            self.new_game.all_position, self.new_game.path,
            self.show_items.path_graph
        )
        self.show_items.add_graph(
            self.new_game.all_position, self.new_game.wall,
            self.show_items.wall_graph
        )
        self.show_items.add_graph(
            self.new_game.all_position,
            self.new_game.gard_localisation,
            self.show_items.gard_graph,
        )
        self.show_items.add_graph(
            self.new_game.all_position,
            self.new_game.exit_localisation,
            self.show_items.exit_graph,
        )
        self.show_items.add_graph(
            self.new_game.all_position,
            self.labyrinth.stuff1_localisation,
            self.show_items.stuff1_graph,
        )
        self.show_items.add_graph(
            self.new_game.all_position,
            self.labyrinth.stuff2_localisation,
            self.show_items.stuff2_graph,
        )
        self.show_items.add_graph(
            self.new_game.all_position,
            self.labyrinth.stuff3_localisation,
            self.show_items.stuff3_graph,
        )
        self.show_items.add_graph(
            self.new_game.all_position,
            self.new_game.hero_localisation,
            self.show_perso.hero_graph,
        )
        self.show_perso.built_inventory(
            self.show_items.surface_game, self.perso.inventory
        )

    def add_lvl_counter(self):
        """ add graphical "lvl counter" to know where are we"""
        self._show_new_game.show_actual_lvl(
            self._show_items.surface_game, self.new_game.actual_level
        )

    def refresh(self):
        """ actualise pygame window """
        pygame.display.flip()
