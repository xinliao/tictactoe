board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]


def instructions():
    print("welcome to the game tic tac toe")
    print("the game will be displayed like this")
    print(" / / ")
    print(" / / ")
    print(" / / ")
    print("to enter the postion of your (X) AND (O)")
    print("simply enter the number corresponding to the postion of the board")
    print("7/8/9")
    print("4/5/6")
    print("1/2/3")


from IPython.display import clear_output


def display_board(board):
    print(board[7] + "/" + board[8] + "/" + board[9])
    print(board[4] + "/" + board[5] + "/" + board[6])
    print(board[1] + "/" + board[2] + "/" + board[3])


def player1_choice_tictactoe():
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        choice = input("player 1 please select your baord position: ")
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("please select a number from 1-9")
        return int(choice)


def player2_choice_tictactoe():
    choice = ""
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        choice = input("player 2 please select your baord position: ")
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("please select a number from 1-9")
    return int(choice)


def replacement_choice(board, position):
    user_placement = input("type X or Y to replace the position:")
    board[position] = user_placement

    return board


def youwin(board):
    # horizontal
    if board[1] == board[2] and board[2] == board[3]:
        return "you win"
    if board[1] == board[2] and board[2] == board[3]:
        return "you win"
    if board[1] == board[2] and board[2] == board[3]:
        return "you win"
    # vertical
    if board[1] == board[4] and board[4] == board[7]:
        return "you win"
    if board[2] == board[5] and board[5] == board[8]:
        return "you win"
    if board[3] == board[6] and board[6] == board[9]:
        return "you win"
    # x
    if board[1] == board[5] and board[5] == board[9]:
        return "you win"
    if board[7] == board[5] and board[5] == board[3]:
        return "you win"


game_on = True
board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

while game_on:

    instructions()

    display_board(board)
    # player 1 turn
    position = player1_choice_tictactoe()

    board = replacement_choice(board, position)
    # show board
    display_board(board)
    # player 2 turn
    position = player2_choice_tictactoe()

    board = replacement_choice(board, position)
    # show board
    display_board(board)

    youwin(board)
