import threading
import random
#2d array
Game_board = [
    [' ','|',' ','|',' '],
    ['-','-','-','-','-'],
    [' ','|',' ','|',' '],
    ['-','-','-','-','-'],
    [' ','|',' ','|',' ']
]

Player1_turn = True
Game_Over = False

player1_piece = 'x'
player2_piece = 'o'
#print 2d array
def print_board():
    global Game_board
    for row in Game_board:
        for element in row:
            print(element, end="")
        print()
    print('\n')
#array storing avaible moves

Available_moves = [(0,0),(0,2),(0,4)
                   ,(2,0),(2,2),(2,4),
                   (4,0),(4,2),(4,4)]
#method for a player/s turn.



def check_game_over(piece : str) -> bool:
    global Game_board
    global Game_Over
    global Available_moves
    if len(Available_moves) <= 0:
        Game_Over = True
        return True
    #check rows
    for row in range(3):
        if Game_board[row*2][0] == Game_board[row*2][2] == Game_board[row*2][4] == piece:
            Game_Over = True
            return True
    #check columns
    for column in range(3):
        if Game_board[0][column*2] == Game_board[2][column*2] == Game_board[4][column*2] == piece:
            Game_Over = True
            return True
    #check diagonal

    if Game_board[0][0] == Game_board[2][2] == Game_board[4][4] == piece:
        Game_Over = True
        return True
    
    if Game_board[4][0] ==Game_board[2][2] == Game_board[0][4] == piece:
        Game_Over = True
        return True
    return False
def Place_piece(piece : str):
    global Available_moves
    global Game_board
    if len(Available_moves) > 0:
        i = Available_moves[random.randint(0,len(Available_moves)-1)]

        row = i[0]
        column = i[1]
        
        Game_board[row][column] = piece
        Available_moves.remove(i,)    
    check_game_over(piece)

while(not Game_Over):
    Place_piece(player1_piece)
    print_board()
    if not Game_Over:
        Place_piece(player2_piece)
        print_board()