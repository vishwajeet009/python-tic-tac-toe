print("========================================================================")
print("                           TIC_TAC_TOE                                  ")
print("========================================================================\n")
print("Choose Type :\n")
print("1.Vs CPU")
print("2.Vs Player\n")
print("========================================================================\n")

choice=int(input())

x=[['1' , '2' , '3'],['4' , '5' , '6'],['7' , '8' , '9']]
print('Board_Position:')

def replace1(pos):
    if pos==1:
        x[0][0]='O'
    if pos==2:
        x[0][1]='O'
    if pos==3:
        x[0][2]='O'
    if pos==4:
        x[1][0]='O'
    if pos==5:
        x[1][1]='O'
    if pos==6:
        x[1][2]='O'
    if pos==7:
        x[2][0]='O'
    if pos==8:
        x[2][1]='O'
    if pos==9:
        x[2][2]='O'

def replace2(pos):
    if pos==1:
        x[0][0]='X'
    if pos==2:
        x[0][1]='X'
    if pos==3:
        x[0][2]='X'
    if pos==4:
        x[1][0]='X'
    if pos==5:
        x[1][1]='X'
    if pos==6:
        x[1][2]='X'
    if pos==7:
        x[2][0]='X'
    if pos==8:
        x[2][1]='X'
    if pos==9:
        x[2][2]='X'
def end():
    for i in x:
        print(i)
    print("\nThe Computer has won!!!")
    exit(0)
for i in x:
    print(i)

def draw():
    for i in x:
        print(i)
    print("\nCongrats, Game ended in a Draw!!!")
    exit(0)
def p1():
    print("\nplayer 1 turn :")
    x=int(input())
    if(x not in range (1,10)):
        print("Invalid input")
        exit(0)
    else:
        replace2(x)
def p2():
    print("\nplayer 2 turn :")
    x=int(input())
    if(x not in range (1,10)):
        print("Invalid input")
        exit(0)
    else:
        replace1(x)
def chkw():
    for i in range (0,3):
        if x[0][i]==x[1][i]==x[2][i]=='X':
            for i in x:
                print(i)
            print("\nPlayer 1 won!")
            exit()
        if x[0][i]==x[1][i]==x[2][i]=='O':
            for i in x:
                print(i)
            print("\nPlayer 2 won!")
            exit()
        if x[i][0]==x[i][1]==x[i][2]=='X':
            for i in x:
                print(i)
            print("\nPlayer 1 won!")
            exit()
        if x[i][0]==x[i][1]==x[i][2]=='O':
            for i in x:
                print(i)
            print("\nPlayer 2 won!")
            exit()
    if(x[0][0]==x[1][1]==x[2][2]=='X'):
            for i in x:
                print(i)
            print("\nPlayer 1 won!")
            exit()
    if(x[0][0]==x[1][1]==x[2][2]=='O'):
            for i in x:
                print(i)
            print("\nPlayer 2 won!")
            exit()
    if(x[0][2]==x[1][1]==x[2][0]=='X'):
            for i in x:
                print(i)
            print("\nPlayer 1 won!")
            exit()    
    if(x[0][2]==x[1][1]==x[2][0]=='O'):
            for i in x:
                print(i)
            print("\nPlayer 2 won!")
            exit()  
print("RULES:")
print("A. Tap Desired Position As Input :")
print("B. (1,4,7),(2,5,8),(3,6,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,5,7) Are Winning Combos !")
print("C. If Either Side Fails To Acheive The Above Combos , The Game Ends In A Draw !")
    


if(choice==1):
    print("\nEnter 1st Move: ")
    move1=int(input())
    if move1 in range (1,10) and move1!=5 :
        cpum1=5
        x[1][1]='X'
        replace1(move1)
        
    else:
        cpum1=1
        x[1][1]='O'
        x[0][0]='X'
    print("CPU Marked at Number:",cpum1,"\n")

    print("Board:\n")
    for i in x:
          print(i)
    print("\nEnter 2nd Move:")
    move2=int(input())
    if move2 in range (1,10) and move1!=5 and move2!=move1:
        replace1(move2)
        if(move1==1):
            if move2==2:
                cpum2=3
            elif move2==3:
                cpum2=2
            elif move2==4:
                cpum2=7
            elif move2==6:
                cpum2=3
            elif move2==7:
                cpum2=4
            elif move2==8:
                cpum2=7
            elif move2==9:
                cpum2=4
        if(move1==2):
            if move2==1:
                cpum2=3
            elif move2==3:
                cpum2=1
            elif move2==4:
                cpum2=1
            elif move2==6:
                cpum2=3
            elif move2==7:
                cpum2=1
            elif move2==8:
                cpum2=4
            elif move2==9:
                cpum2=3
        if(move1==3):
            if move2==2:
                cpum2=1
            elif move2==1:
                cpum2=2
            elif move2==4:
                cpum2=1
            elif move2==6:
                cpum2=9
            elif move2==7:
                cpum2=8
            elif move2==8:
                cpum2=9
            elif move2==9:
                cpum2=6
        if(move1==4):
            if move2==2:
                cpum2=1
            elif move2==3:
                cpum2=1
            elif move2==1:
                cpum2=7
            elif move2==6:
                cpum2=2
            elif move2==7:
                cpum2=1
            elif move2==8:
                cpum2=7
            elif move2==9:
                cpum2=7
        if(move1==6):
            if move2==2:
                cpum2=3
            elif move2==3:
                cpum2=9
            elif move2==4:
                cpum2=2
            elif move2==1:
                cpum2=3
            elif move2==7:
                cpum2=9
            elif move2==8:
                cpum2=9
            elif move2==9:
                cpum2=3
        if(move1==7):
            if move2==2:
                cpum2=1
            elif move2==3:
                cpum2=2
            elif move2==4:
                cpum2=1
            elif move2==6:
                cpum2=9
            elif move2==1:
                cpum2=4
            elif move2==8:
                cpum2=9
            elif move2==9:
                cpum2=8

        if(move1==8):
            if move2==2:
                cpum2=4
            elif move2==3:
                cpum2=9
            elif move2==4:
                cpum2=7
            elif move2==6:
                cpum2=9
            elif move2==7:
                cpum2=9
            elif move2==1:
                cpum2=7
            elif move2==9:
                cpum2=7
        if(move1==9):
            if move2==2:
                cpum2=3
            elif move2==3:
                cpum2=6
            elif move2==4:
                cpum2=7
            elif move2==6:
                cpum2=3
            elif move2==7:
                cpum2=8
            elif move2==8:
                cpum2=7
            elif move2==1:
                cpum2=4
        replace2(cpum2)
    
    elif move2==move1:
        print('invalid move!')
        
    else:
        if move2==2:
            cpum2=8
        elif move2==3:
            cpum2=7
        elif move2==4:
            cpum2=6
        elif move2==6:
            cpum2=4
        elif move2==7:
            cpum2=3
        elif move2==8:
            cpum2=2
        elif move2==9:
            cpum2=3
        replace2(cpum2)
        replace1(move2)
    
    print("CPU Marked at Number:",cpum2,"\n")
    for i in x:
        print(i)
    print('\nEnter 3rd Move:')
    move3=int(input())
    if move3 in range (1,10) and move1!=5 and move2!=move1 and move1!=move3 and move2!=move3:
        replace1(move3)
        if(move1==1):
            if move2==2:
                if move3==7:
                    cpum3=4
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==3:
                if move3==8:
                    cpum3=6
                else:
                    cpum3=8
                    replace2(8)
                    end()
            elif move2==4:
                if move3==3:
                    cpum3=2
                else:
                    cpum3=3
                    replace2(3)
                    end()
            elif move2==6:
                if move3==7:
                    cpum3=4
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==7:
                if move3==6:
                    cpum3=2
                else:
                    cpum3=6
                    replace2(6)
                    end()
            elif move2==8:
                if move3==3:
                    cpum3=2
                else:
                    cpum3=3
                    replace2(3)
                    end()
                
            elif move2==9:
                if move3==6:
                    cpum3=3
                else:
                    cpum3=6
                    replace2(6)
                    end()
        if(move1==2):
            if move2==1:
                if move3==7:
                    cpum3=4
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==3:
                if move3==9:
                    cpum3=6
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==4:
                if move3==9:
                    cpum3=3
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==6:
                if move3==7:
                    cpum3=1
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==7:
                if move3==9:
                    cpum3=8
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==8:
                if move3==6:
                    cpum3=1
                else:
                    cpum3=6
                    replace2(6)
                    end()
            elif move2==9:
                if move3==7:
                    cpum3=8
                else:
                    cpum3=7
                    replace2(7)
                    end()
        if(move1==3):
            if move2==2:
                if move3==9:
                    cpum3=6
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==1:
                if move3==8:
                    cpum3=8
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==4:
                if move3==9:
                    cpum3=6
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==6:
                if move3==1:
                    cpum3=2
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==7:
                if move3==2:
                    cpum3=1
                else:
                    cpum3=2
                    replace2(2)
                    end()
            elif move2==8:
                if move3==1:
                    cpum3=2
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==9:
                if move3==4:
                    cpum3=2
                else:
                    cpum3=4
                    replace2(4)
                    end()
        if(move1==4):
            if move2==2:
                if move3==9:
                    cpum3=7
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==3:
                if move3==9:
                    cpum3=6
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==1:
                if move3==3:
                    cpum3=2
                else:
                    cpum3=3
                    replace2(3)
                    end()
            elif move2==6:
                if move3==8:
                    cpum3=9
                else:
                    cpum3=8
                    replace2(8)
                    end()
            elif move2==7:
                if move3==9:
                    cpum3=8
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==8:
                if move3==7:
                    cpum3=4
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==9:
                if move3==7:
                    cpum3=4
                else:
                    cpum3=7
                    replace2(7)
                    end()
        if(move1==6):
            if move2==2:
                if move3==7:
                    cpum3=9
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==3:
                if move3==1:
                    cpum3=2
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==4:
                if move3==8:
                    cpum3=7
                else:
                    cpum3=8
                    replace2(8)
                    end()
            elif move2==1:
                if move3==8:
                    cpum3=7
                else:
                    cpum3=8
                    replace2(8)
                    end()
            elif move2==7:
                if move3==1:
                    cpum3=4
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==8:
                if move3==1:
                    cpum3=7
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==9:
                if move3==7:
                    cpum3=8
                else:
                    cpum3=7
                    replace2(7)
                    end()
        if(move1==7):
            if move2==2:
                if move3==9:
                    cpum3=8
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==3:
                if move3==8:
                    cpum3=9
                else:
                    cpum3=8
                    replace2(8)
                    end()
            elif move2==4:
                if move3==9:
                    cpum3=8
                else:
                    cpum3=9
                    replace2(9)
                    end()
            elif move2==6:
                if move3==1:
                    cpum3=4
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==1:
                if move3==6:
                    cpum3=2
                else:
                    cpum3=6
                    replace2(6)
                    end()
            elif move2==8:
                if move3==1:
                    cpum3=4
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==9:
                if move3==2:
                    cpum3=4
                else:
                    cpum3=2
                    replace2(2)
                    end()

        if(move1==8):
            if move2==2:
                if move3==6:
                    cpum3=1
                    if move4==7:
                        cpum4=9
                    else:
                        cpum4=7
                    replace2(cpum3)
                    replace2(cpum4)
                    end()
                    
                else:
                    cpum3=6
                    replace2(6)
                    end()
            elif move2==3:
                if move3==1:
                    cpum3=2
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==4:
                if move3==3:
                    cpum3=1
                else:
                    cpum3=3
                    replace2(3)
                    end()
            elif move2==6:
                if move3==1:
                    cpum3=3
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==7:
                if move3==1:
                    cpum3=4
                else:
                    cpum3=1
                    replace2(1)
                    end()
            elif move2==1:
                if move3==3:
                    cpum3=2
                else:
                    cpum3=3
                    replace2(3)
                    end()
            elif move2==9:
                if move3==3:
                    cpum3=2
                else:
                    cpum3=3
                    replace2(3)
                    end()
        if(move1==9):
            if move2==2:
                if move3==7:
                    cpum3=8
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==3:
                if move3==4:
                    cpum3=2
                else:
                    cpum3=4
                    replace2(4)
                    end()
            elif move2==4:
                if move3==3:
                    cpum3=6
                else:
                    cpum3=3
                    replace2(3)
                    end()
            elif move2==6:
                if move3==7:
                    cpum3=8
                else:
                    cpum3=7
                    replace2(7)
                    end()
            elif move2==7:
                if move3==2:
                    cpum3=4
                else:
                    cpum3=2
                    replace2(2)
                    end()
            elif move2==8:
                if move3==3:
                    cpum3=6
                else:
                    cpum3=3
                    replace2(3)
                    end()
            elif move2==1:
                if move3==6:
                    cpum3=3
                else:
                    cpum3=6
                    replace2(6)
                    end()
        replace2(cpum3)
    
    elif move3==move1 or move3==move2:
        print('invalid move!')
        
    else:
        if move2==2:
            if move3==4:
                cpum3=6
            elif move3==7:
                cpum3=3
            elif move3==3:
                cpum3=7
            elif move3==6:
                cpum3=4
            elif move3==9:
                cpum3=4
        elif move2==3:
            if move3==4:
                cpum3=6
            else:
                cpum3=4
                replace1(4)
                end()
        elif move2==4:
            if move3==2:
                cpum3=8
            elif move3==7:
                cpum3=3
            elif move3==3:
                cpum3=7
            elif move3==8:
                cpum3=2
            elif move3==9:
                cpum3=3
                
        elif move2==6:
            if move3==7:
                cpum3=3
            else:
                cpum3=7
                replace1(7)
                end()
        elif move2==7:
            if move3==2:
                cpum3=8
            else:
                cpum3=2
                replace1(2)
                end()
        elif move2==8:
            if move3==3:
                cpum3=7
            else:
                cpum3=3
        elif move2==9:
            if move3==2:
                cpum3=8
            else:
                cpum3=2
                replace1(2)
                end()
        replace2(cpum3)
        replace1(move3)
    print("CPU Marked at Number:",cpum3,"\n")
    for i in x:
        print(i)
    print('\nEnter 4th Move:')
    move4=int(input())
    if move4 in range (1,10) and move2!=move1 and move1!=move3 and move2!=move3 and move1!=move4 and move2!=move4 and move3!=move4:
        replace1(move4)
        a=[1,2,3,4,5,6,7,8,9]
        b=[move1,move2,move3,move4,cpum1,cpum2,cpum3]
        c=[]
        for i in a:
            if i not in b:
               c.append(i)
    else:
        print("Invalid move")
        exit(0)
    print("CPU Marked at Number:",c[0],"\n")
    replace2(c[0])
    replace1(c[1])
    draw()

if choice==2:
    p1()
    for i in x:
          print(i)
    p2()
    for i in x:
          print(i)
    p1()
    for i in x:
          print(i)
    p2()
    for i in x:
          print(i)
    p1()
    chkw()
    for i in x:
          print(i)
    p2()
    chkw()
    for i in x:
          print(i)
    p1()
    chkw()
    for i in x:
          print(i)
    p2()
    chkw()
    for i in x:
          print(i)
    print("Draw...Better luck Next time noobies")
    
    
    
        
    
    
    


