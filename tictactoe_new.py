import random

marker = ""


def display_board(board):
    print(board[1] + "/" + board[2] + "/" + board[3])
    print(board[4] + "/" + board[5] + "/" + board[6])
    print(board[7] + "/" + board[8] + "/" + board[9])


def player_input():

    playerinput = " "

    while playerinput not in ["X", "O"]:
        playerinput = input("Please select either X or O: ")
    player_1 = playerinput
    if playerinput == "X":
        player_1 = "X"
        player_2 = "0"
    else:
        player_2 = "X"
    return (player_1, player_2)


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, marker):
    # horizontal
    if board[1] == board[2] == board[3] == marker:
        return True
    if board[4] == board[5] == board[6] == marker:
        return True
    if board[7] == board[8] == board[9] == marker:
        return True
    # vertical
    if board[1] == board[4] == board[7] == marker:
        return True
    if board[2] == board[5] == board[8] == marker:
        return True
    if board[3] == board[6] == board[9] == marker:
        return True
    # xs
    if board[1] == board[5] == board[9] == marker:
        return True
    if board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


def choose_first():
    player = random.randint(1, 2)
    if player == 1:
        print("Player 1 go first")
    if player == 2:
        print("PlayYer 2 go first")


def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False


def full_board_check(board):
    if (
        board[1]
        and board[2]
        and board[3]
        and board[4]
        and board[5]
        and board[6]
        and board[7]
        and board[8]
        and board[9] != " "
    ):
        return True
    else:
        return False


def player_choice(board):
    choice = " "
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        choice = input("Please select a number from 1-9: ")
        return int(choice)

    space_check(board, choice)
    space_free = space_check(board, choice)
    if space_free:
        return choice
    else:
        return None


def replay():
    answer = ""
    while answer not in ["Y", "N"]:
        answer = input("Continue? Please select Y or N: ")
    if answer == "Y":
        return True
    else:
        return False


# def the_end():
#     end = win_check(board, player_1_marker, player_2_marker)
#     if end == True:
#         print("Congrulations!", marker, "You have won!")


# def continue_():
#     end = win_check(board, player_1_marker, player_2_marker)
#     if end == True:
#         return replay()


game_on = True
print("Welcome to Tic Tac Toe!")

while True:
    print("\n" * 100)
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    print(" ")
    print(" ")
    choose_first()
    print(" ")
    player_1_marker, player_2_marker = player_input()

    while game_on:
        display_board(board)

        # player1 turn
        player_1_position = player_choice(board)
        place_marker(board, player_1_marker, player_1_position)
        if win_check(board, player_1_marker):
            print("Congragulations! Player 1 you have won!")
            break
        if full_board_check(board):
            print("Sorry the board is full")
            break
        display_board(board)

        # player_2_turn
        player_2_position = player_choice(board)
        place_marker(board, player_2_marker, player_2_position)

        if full_board_check(board):
            print("Sorry the board is full")
            break
        if win_check(board, player_2_marker):
            print("Congragulations! Player 2 you have won!")
            break

    if not replay():
        break

        # the_end()
        # continue_()

