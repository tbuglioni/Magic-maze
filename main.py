from logic.Game import Game


def main():
    my_game = Game()
    my_game.init_game(1)

    while my_game.boucle_statut:
        my_game.all_event()
        my_game.interaction_game()
        my_game.check_end()
        my_game.graph_all()
        my_game.add_lvl_counter()
        my_game.refresh()


if __name__ == "__main__":
    main()
