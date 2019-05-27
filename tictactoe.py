'''
def main():
    lst=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    print("HELLO! AND WELCOME TO TIC TAC TOE")
    player1=input("What would player 1 like to be? x or o?")
    if player1=='x':
        player2='o'
    else:
        player2='x'
        
    print("Alright, player one goes first.")

    pos=int(input("Enter your position: "))
    
       
    if pos==1:
        lst[2][0]='X'
    elif pos==2:
        lst[2][1]='X'
    elif pos==3:
        lst[2][2]='X'
    elif pos==4:
        lst[1][0]='X'
    elif pos==5:
        lst[1][1]='X'
    elif pos==6:
        lst[1][2]='X'
    elif pos==7:
        lst[0][0]='X'
    elif pos==8:
        lst[0][1]='X'
    elif pos==9:
        lst[0][2]='X'
        

    print(lst[0][0]+" | "+lst[0][1]+" | "+lst[0][2])
    print("---------")
    print(lst[1][0]+" | "+lst[1][1]+" | "+lst[1][2])
    print("---------")
    print(lst[2][2]+" | "+lst[2][1]+" | "+lst[2][0])
'''
