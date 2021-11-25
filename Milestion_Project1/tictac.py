from main import *
print ("Welcome to Tic Toc Game")

while True:
    theBoard = [' '] * 10
    player_1, player_2 = player_input()
    turn = choose_first()
    print(turn + "Will go first")

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display_board(theBoard)
            pos = player_choice(theBoard)
            place_marker(theBoard,player_1,pos)

            if win_check(theBoard, player_1):
                display_board(theBoard)
                print("You are The Winner Player 1!!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player2'
        else :
            display_board(theBoard)
            pos = player_choice(theBoard)
            place_marker(theBoard,player_2,pos)

            if win_check(theBoard,player_2):
                display_board(theBoard)
                print("You are The Winner Player 2!!")
                game_on = False 
            else :
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is a draw!")
                    break
                else :
                    turn = 'player1'
    if not replay():
        break




