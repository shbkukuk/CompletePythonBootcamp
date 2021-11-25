import random

def display_board(board):
    print('\n'*100)

    print('   |   |')
    print(' '+ board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(board)


def player_input():
    mark = ""

    while not (mark == 'X' or mark =='O'):
        mark = input("Player1: Do you want to be 'X' or 'O' :").upper()

    if mark == 'X':
        return ('X','O')
    else :
        return ('O','X')

# player_input()
def place_marker(board,marker,position):
    board[position] = marker

# place_marker(board,'$',8)
# display_board(board)
def win_check(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9] == mark) or
    (board[4]==mark and board[5]==mark and board[6] == mark)or
    (board[1]==mark and board[2]==mark and board[3] == mark)or
    (board[7]==mark and board[4]==mark and board[1] == mark)or
    (board[8]==mark and board[5]==mark and board[2] == mark)or
    (board[9]==mark and board[6]==mark and board[3] == mark)or
    (board[7]==mark and board[5]==mark and board[3] == mark)or
    (board[9]==mark and board[5]==mark and board[1] == mark))

# a = win_check(board,'X')
# print(a)
def choose_first():
    player = random.randint(1,2)
    if player == 1:
        return 'player1'
    else :
        return 'player2'

def space_check(board,position):
    return (board[position] == ' ')

def full_board_check(board):
    for pos in range(1,10):
        if space_check(board,pos): 
            return False 
        
    return True
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')