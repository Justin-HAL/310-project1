import threading
import random
import time

#2d array
Game_board = [
    [' ','|',' ','|',' '],
    ['-','-','-','-','-'],
    [' ','|',' ','|',' '],
    ['-','-','-','-','-'],
    [' ','|',' ','|',' ']
]

Game_Over = False

mutex_lock = threading.Lock()

#array storing avaible moves
Available_moves = [(0,0),(0,2),(0,4),
                   (2,0),(2,2),(2,4),
                   (4,0),(4,2),(4,4)]
#method for a player/s turn.

# Condition variable 
condition = threading.Condition()
turn = 'X'  

#print 2d array
def print_board():
    global Game_board
    for row in Game_board:
        for element in row:
            print(element, end="")
        print()
    print('\n')


def check_game_won(piece: str) -> bool:
    global Game_board
    global Available_moves

    # Check rows
    for row in range(3):
        if Game_board[row*2][0] == Game_board[row*2][2] == Game_board[row*2][4] == piece:
            Game_Over = True
            return True
    # Check columns
    for column in range(3):
        if Game_board[0][column*2] == Game_board[2][column*2] == Game_board[4][column*2] == piece:
            Game_Over = True
            return True

    # Check diagonals
    if Game_board[0][0] == Game_board[2][2] == Game_board[4][4] == piece:
        Game_Over = True
        return True
    if Game_board[4][0] == Game_board[2][2] == Game_board[0][4] == piece:
        Game_Over = True
        return True
    return False

def Place_piece(piece: str):
    global Available_moves
    global Game_board
    global Game_Over
    if len(Available_moves) > 0 and not Game_Over:
        move = random.choice(Available_moves)
        row, column = move
        Game_board[row][column] = piece
        Available_moves.remove(move)

def player_thread(piece: str):
    global Game_Over
    global condition
    global turn
    time.sleep(0.5)
    while not Game_Over:
        with condition:
            while turn != piece and not Game_Over:
                condition.wait()
            if Game_Over:
                condition.notify_all()
                break
            # Player's turn
            mutex_lock.acquire()
            print(f"Player {piece} is making a move:")
            Place_piece(piece)
            print_board()
            time.sleep(1)
            if check_game_won(piece):
                print(f"Player {piece} wins!")
                Game_Over = True
                condition.notify_all()
                break
            elif len(Available_moves) == 0:
                print("It's a draw!")
                Game_Over = True
                condition.notify_all()
                break
            # Switch turn to the other player
            turn = 'O' if piece == 'X' else 'X'
            condition.notify_all()
            mutex_lock.release()
def main():
    # Create threads for both players
    t1 = threading.Thread(target=player_thread, args=('X',))
    t2 = threading.Thread(target=player_thread, args=('O',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Game Over.")

if __name__ == "__main__":
    main()
