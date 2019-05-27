theBoard=[' ']*10

def player_input():
    choice=input("What would player 1 like to be?: ").upper()
    if choice=='X':
        return('X','O')
    else:
        return('O','X')
    
p1,p2=player_input()

import random
def goes_first():
    return random.randint(1,2)
    
from IPython.display import clear_output

def display_board(board):
    clear_output()    
    print(board[7]+" | "+board[8]+" | "+board[9])
    print('----------')
    print(board[4]+" | "+board[5]+" | "+board[6])
    print('----------')
    print(board[1]+" | "+board[2]+" | "+board[3])    

def space_check():
    pass

def checkmate(mark):
    
    return ((theBoard[7] == mark and theBoard[8] == mark and theBoard[9] == mark) or # across the top
    (theBoard[4] == mark and theBoard[5] == mark and theBoard[6] == mark) or # across the middle
    (theBoard[1] == mark and theBoard[2] == mark and theBoard[3] == mark) or # across the bottom
    (theBoard[7] == mark and theBoard[4] == mark and theBoard[1] == mark) or # down the middle
    (theBoard[8] == mark and theBoard[5] == mark and theBoard[2] == mark) or # down the middle
    (theBoard[9] == mark and theBoard[6] == mark and theBoard[3] == mark) or # down the right side
    (theBoard[7] == mark and theBoard[5] == mark and theBoard[3] == mark) or # diagonal
    (theBoard[9] == mark and theBoard[5] == mark and theBoard[1] == mark)) # diagonal
    
def tie():
    pass

turn=goes_first()
while True:
    if  turn==1:
        print("Player 1 goes")        
        position=int(input("Enter your position: "))
        
        theBoard[position]=p1
        display_board(theBoard)
        turn=2
        if checkmate(p1):
            print("Player 1 WINS!!")
            break
    else:
        print("Player 2 goes")
        position=int(input("Enter your position: "))
        theBoard[position]=p2
        display_board(theBoard)
        turn=1
        if checkmate(p2):
            print("Player 2 WINS!!")
            break
