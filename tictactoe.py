'''def main():
    lst=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    print("HELLO! AND WELCOME TO TIC TAC TOE")
    p1=input("What would player 1 like to be? X or O?")
    if p1=='X':
        p2='O'
    else:
        p2='X'
    count=0    
    print("Alright, player one goes first.")
    
    checkmate=0
    while (checkmate==0):
        pos=int(input("Enter your position: "))
        
        if count%2==0:
          if pos==1:
            lst[2][0]=p1
          elif pos==2:
            lst[2][1]=p1
          elif pos==3:
            lst[2][2]=p1
          elif pos==4:
            lst[1][0]=p1
          elif pos==5:
            lst[1][1]=p1
          elif pos==6:
            lst[1][2]=p1
          elif pos==7:
            lst[0][0]=p1
          elif pos==8:
            lst[0][1]=p1
          elif pos==9:
            lst[0][2]=p1
        else:
          if pos==1:
            lst[2][0]=p2
          elif pos==2:
            lst[2][1]=p2
          elif pos==3:
            lst[2][2]=p2
          elif pos==4:
            lst[1][0]=p2
          elif pos==5:
            lst[1][1]=p2
          elif pos==6:
            lst[1][2]=p2
          elif pos==7:
            lst[0][0]=p2
          elif pos==8:
            lst[0][1]=p2
          elif pos==9:
            lst[0][2]=p2
        
        count+=1
        
        print(lst[0][0]+" | "+lst[0][1]+" | "+lst[0][2])
        print("---------")
        print(lst[1][0]+" | "+lst[1][1]+" | "+lst[1][2])
        print("---------")
        print(lst[2][2]+" | "+lst[2][1]+" | "+lst[2][0])
        
        for x in range(3):
            if (lst[x][0]==lst[x][1]==lst[x][2]=='X'):
                    checkmate=1
                    print("Player 1 WON HORIZONTAL!!")
            elif((lst[x][0]==lst[x][1]==lst[x][2]=='O')):
                    checkmate=1
                    print("Player 2 WON!!")
        for x in range (3):
            if (lst[x][x]==lst[x][x]==lst[x][x]=='X'):
                    checkmate=1
                    print("Player 1 WON DIAGNOL!!")
            elif((lst[x][x]==lst[x][x]==lst[x][x]=='O')):
                    checkmate=1
                    print("Player 2 WON!!")
        for x in range(3):
            if (lst[0][abs(x-2)]==lst[1][abs(x-2)]==lst[2][x]=='X'):
                    checkmate=1
                    print("Player 1 WON VERTICAL!!")
            elif(lst[0][abs(x-2)]==lst[1][abs(x-2)]==lst[2][x]=='O'):
                    checkmate=1
                    print("Player 2 WON!!")
            
main()'''
