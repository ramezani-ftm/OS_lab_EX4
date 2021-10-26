import random
import time
from colorama import Fore


def show_game():
    for i in range(3):
        for j in range(3):
            if game[i][j]=='O':
                print(Fore.RED + game[i][j] , Fore.RESET , end=' ')
            elif game[i][j]=='X':
                print(Fore.GREEN + game[i][j] , Fore.RESET , end=' ')
            else:
                print( game[i][j] , Fore.RESET , end=' ' )

        print(Fore.RESET)


def check_scor_x():
    scor_x = 0
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 'X':
            scor_x = 1
            break
        if game[0][i] == game[1][i] == game[2][i] == 'X':
            scor_x = 1
            break
        if game[0][0] == game[1][1] == game[2][2] == 'X':
            scor_x = 1
            break
        if game[0][2] == game[1][1] == game[2][0] == 'X':
            scor_x = 1
            break
    return scor_x

def check_scor_o():
    scor_o = 0
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 'O':
            scor_o = 1
            break
        if game[0][i] == game[1][i] == game[2][i] == 'O':
            scor_o = 1
            break
        if game[0][0] == game[1][1] == game[2][2] == 'O':
            scor_o = 1
            break
        if game[0][2] == game[1][1] == game[2][0] == 'O':
            scor_o = 1
            break
    return scor_o

start = 0

def check_win():
    o = check_scor_o()
    x = check_scor_x()
           
    if o > x:
        print('o win')
        print('Game time: ' + str(time.time()-start) , 's')
        exit()
    elif o < x:
        print('x win')
        print('Game time: ' + str(time.time()-start) , 's')
        exit()
    else:
        flag = 1
        for i in range(3):
            for j in range(3):
                if game[i][j]=='-':
                    flag = 0
        
        if  flag ==1 and o == x:
            print('mosavi')
            print('Game time: ' + str(time.time()-start) , 's')
            exit()
     

game = [['-' ,'-' , '-' ],
        ['-' ,'-' , '-' ],
        ['-' ,'-' , '-' ]]
    
start = time.time()

choice = int(input('''Please Take a Choice:
1.player 1  &  player 2
2.player  &  computer 
'''))

if choice == 1:

    while True:
            
        #player 1   
        while True:
            row = int(input('row : '))
            col = int(input('col : '))

            if 0 <= row <= 2 and 0<= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'X'
                    break
                else:
                    print('this cell is not empty')
                break
            else:
                print('invalid inputs, row and col must be between 0 , 2')
        
        show_game()
        check_win()
        
        #player 2 
        while True:
            row = int(input('row : '))
            col = int(input('col : '))

            if 0 <= row <= 2 and 0<= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'O'
                    break
                else:
                    print('this cell is not empty')
            else:
                print('invalid inputs, row and col must be between 0 , 2')
        
        show_game()
        check_win()

else :
    while True:
            
        #player  
        while True:
            row = int(input('row : '))
            col = int(input('col : '))

            if 0 <= row <= 2 and 0<= col <= 2:
                if game[row][col]=='-':
                    game[row][col] = 'X'
                    break
                else:
                    print('this cell is not empty')
                break
            else:
                print('invalid inputs, row and col must be between 0 , 2')
        
        show_game()
        check_win()
        

        
        #computer
        print('computer :') 
        while True:
            
            row = random.randint(0 , 2)
            col = random.randint(0 , 2)

            if game[row][col]=='-':
                game[row][col] = 'O'
                break

        show_game()
        check_win()
