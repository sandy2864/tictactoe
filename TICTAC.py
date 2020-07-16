#from IPython.display import clear_output
def display_board(board):
    #clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('----------')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('----------')
    print(board[1]+' | '+board[2]+' | '+board[3])
def player_input():
    '''
    OUTPUT=(player1 marker,player2 marker)
    '''
    marker=' '
    while  marker!='X' and marker!= 'O':
        marker=input('Player1: choose X or O')
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
def place_marker(board,marker,position):
    board[position]=marker
def win_tic(board,mark):
    return( (board[7]==board[8]==board[9]==mark) or
                (board[4]==board[5]==board[6]==mark) or
                (board[1]==board[2]==board[3]==mark) or
                (board[7]==board[4]==board[1]==mark) or
                (board[8]==board[5]==board[2]==mark) or
                (board[9]==board[6]==board[3]==mark) or
                (board[7]==board[5]==board[3]==mark) or
                (board[1]==board[5]==board[9]==mark))
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board,position):
    return  board[position]==' '
def Full_check(new_board):
    for i in range(1,10):
        if  space_check(new_board,i):
            return False
    return True
def player_choice(new_board):
    position=0
    while  position not in [1,2,3,4,5,6,7,8,9] or not  space_check(new_board,position):
        position=int(input('enter the position (1-9): '))
    return position
def replay():
    choice=input('if you wanna play again type Yes')
    return choice=='Yes'
print("Welcome to TIC-TAC-TOE")
while True:
    #setting up the board,marker,toss
    new_board=[' ']*10
    player1_marker, player2_marker=player_input()
    turn =choose_first()
    print(turn+ ' will go first')
    play_game=input('Ready to play? choose y or n')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player 1':
            display_board(new_board)
            position=player_choice(new_board)
            place_marker(new_board,player1_marker,position)
            if win_tic(new_board,player1_marker):
                display_board(new_board)
                print('Player 1 won!!!!!!!!!!!')
                game_on=False
            else:
                if Full_check(new_board):
                    display_board(new_board)
                    print('TIE GAME')
                    game_on=False
                else:
                    turn='player 2'
        else:
            display_board(new_board)
            position=player_choice(new_board)
            place_marker(new_board,player2_marker,position)
            if win_tic(new_board,player2_marker):
                display_board(new_board)
                print('Player 2 won!!!!!!!!!!!')
                game_on=False
            else:
                if Full_check(new_board):
                    display_board(new_board)
                    print('TIE GAME')
                    game_on=False
                else:
                    turn='player 1'
                    
    if not replay():
        break