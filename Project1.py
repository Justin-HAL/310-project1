import threading

#2d array
Game_board = [
    [' ','|',' ','|',' '],
    ['-','-','-','-','-'],
    [' ','|',' ','|',' '],
    ['-','-','-','-','-'],
    [' ','|',' ','|',' ']
]
#turn order bool?
Player1_turn = True
#print 2d array
def print_board():
    global Game_board
    for row in Game_board:
        for element in row:
            print(element, end="")
        print()
#array storing avaible moves

#method for a player/s turn.


