import os
import pprint

game_running: bool = True
game_started: bool = False

board: list[list[int]] = []
board_rows: int = 6
board_columns: int = 7

players: int = 2
player_to_move: int = 0
column_submitted: bool = False
winner: int = 1


def config_valid():
    global game_running

    if players < 2:
        print("\nPlayer number should be equal to 2 or greater than 2\n")
        game_running = False
        return False

    if board_columns < 4 or board_rows < 4:
        print("\nBoard should have at least 4 rows and 4 columns\n")
        game_running = False
        return False

    return True


def init_game():
    global game_started, board

    for _ in range(board_rows):
        new_row: list[int] = []

        for _ in range(board_columns):
            new_row.append(0)

        board.append(new_row)

    game_started = True


def change_player():
    global player_to_move, players

    if player_to_move + 1 == players:
        player_to_move = 0
    else:
        player_to_move += 1


def print_the_board():
    global column_submitted
    column_submitted = False

    print("\n")
    pprint.pp(board)


def check_win_condition():
    global game_running, winner

    directions: list[tuple[int, int]] = [
        (0, 1),  # horizontal →
        (1, 0),  # vertical ↓
        (1, 1),  # diagonal ↘
        (-1, 1),  # diagonal ↗
    ]

    for i in range(board_rows):
        for j in range(board_columns):
            player: int = board[i][j]
            if player == 0:
                continue

            for dr, dc in directions:
                count: int = 1
                r, c = i, j
                while count < 4:
                    r += dr
                    c += dc
                    if r < 0 or r >= board_rows or c < 0 or c >= board_columns or board[r][c] != player:
                        break
                    count += 1

                if count == 4:
                    print(f"\nWinner is: Player #{player}\n")
                    game_running = False
                    return True

    return False


def check_for_valid_moves():
    global game_running

    for i in range(board_rows):
        for j in range(board_columns):
            if board[i][j] == 0:
                return False

    print("\nGame is a draw. There are no valid moves...\n")
    game_running = False
    return True


def update_board(num: int):
    global board

    if board[board_rows - 1][num] == 0:
        board[board_rows - 1][num] = player_to_move + 1
        return

    for i in range(board_rows - 1, -1, -1):
        if board[i][num] == 0:
            board[i][num] = player_to_move + 1
            return


def player_move():
    print(f"\nPlayer to move: {player_to_move + 1}")
    player_input: int = ask_for_input()

    if player_input == -1:
        return

    update_board(num=player_input)
    change_player()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_for_input() -> int:
    global game_running, column_submitted

    try:
        num: int = int(input("\nEnter a column number: "))

        if num < 0 or num > board_columns:
            print("\nInvalid input, please enter a valid column number.")
            return 0

        column_submitted = True
        return num - 1

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
        if not config_valid():
            return

        init_game()

    print_the_board()

    if check_win_condition():
        return

    if check_for_valid_moves():
        return

    while not column_submitted:
        player_move()

    clear_screen()


if __name__ == '__main__':
    while game_running:
        run_game()
