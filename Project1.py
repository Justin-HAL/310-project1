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
#print 2d array
def print_board():
    global Game_board
    for row in Game_board:
        for element in row:
            print(element, end="")
        print()
#array storing avaible moves

Available_moves = [(0,0),(0,2),(0,4)
                   ,(2,0),(2,2),(2,4),
                   (4,0),(4,2),(4,4)]
#method for a player/s turn.

def Place_piece(piece : str):
    global Available_moves
    global Game_board

    i = Available_moves[random.randint(0,len(Available_moves)- 1)]

    row = i[0]
    column = i[1]
      
    Game_board[row][column] = piece
    Available_moves.remove(i,)

