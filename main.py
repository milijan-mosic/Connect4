def print_the_board():
    pass


def check_win_condition():
    return False


def check_for_valid_moves():
    return False


def player_move():
    pass


def run_game():
    print_the_board()

    if check_win_condition():
        return

    if check_for_valid_moves():
        return

    player_move()


if __name__ == '__main__':
    run_game()
