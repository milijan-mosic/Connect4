import os
import pprint

game_running: bool = True
game_started: bool = False

board: list[list[str]] = []
board_rows: int = 6
board_columns: int = 7

players: int = 2
player_to_move: int = 0
column_submitted: bool = False
winner: int = 1


def init_game():
    global game_started, board

    for _ in range(board_rows):
        new_row: list[str] = []

        for _ in range(board_columns):
            new_row.append('')

        board.append(new_row)

    game_started = True


def print_the_board():
    global column_submitted
    column_submitted = False

    print("\n")
    pprint.pp(board)

    print(f"\nPlayer to move: {player_to_move + 1}")


def check_win_condition():
    return False


def check_for_valid_moves():
    return False


def player_move():
    player_input: int = ask_for_input()

    if player_input == -1:
        return


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_for_input() -> int:
    global game_running, column_submitted

    try:
        num: int = int(input("\nEnter a column number: "))
        column_submitted = True

        return num

    except KeyboardInterrupt:
        print("\nCtrl+C detected. Stopping game...")
        game_running = False
        column_submitted = True

        return -1

    except ValueError:
        print("\nInvalid input, please enter a number.")

        return 0


def run_game():
    if not game_started:
        init_game()

    print_the_board()

    if check_win_condition():
        print(f"\nWinner is: {winner + 1}")
        return

    if check_for_valid_moves():
        print("\nGame is a draw. There are no valid moves...")
        return

    while not column_submitted:
        player_move()

    clear_screen()


if __name__ == '__main__':
    while game_running:
        run_game()
