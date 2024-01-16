from random import randint


# Tic Tac Toe


def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


def player_input():
    # Prompt player if they want X or O
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (board[7] == board[8] == board[9] == mark or
            board[4] == board[5] == board[6] == mark or
            board[1] == board[2] == board[3] == mark or
            board[7] == board[5] == board[3] == mark or
            board[9] == board[5] == board[1] == mark or
            board[7] == board[4] == board[1] == mark or
            board[8] == board[5] == board[2] == mark or
            board[9] == board[6] == board[3] == mark)


def choose_first():
    first_user = randint(1, 2)
    print(f'player {first_user} goes first')
    return first_user


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Pick your position: '))
    return position


def replay():
    play_again = 'wrong'
    while play_again not in ['Y', 'N']:
        play_again = input('Play again? Y or N: ').upper()
    return True if play_again == 'Y' else False


print('Welcome to Tic Tac Toe!')

# while True:
while True:
    board = [' '] * 10
    display_board(board)
    player1, player2 = player_input()
    turn = choose_first()
    # Set the game up here

    # pass
    # while game_on:
    game_on = True
    while game_on:
        # Player 1 Turn
        if turn == 1:
            position = player_choice(board)
            place_marker(board, player1, position)
            display_board(board)
            if win_check(board, player1):
                display_board(board)
                print('Player 1 WON!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a Tie!')
                    game_on = False
                else:
                    turn = 2
        # Player 2 Turn
        else:
            position = player_choice(board)
            place_marker(board, player2, position)
            display_board(board)
            if win_check(board, player2):
                display_board(board)
                print('Player 2 WON!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a Tie!')
                    game_on = False
                else:
                    turn = 1

    if not replay():
        break

    # if not replay():
    # break
    # pass
