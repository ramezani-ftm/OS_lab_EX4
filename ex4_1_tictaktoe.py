import random
from colorama import Fore


def show_game():
    for i in range(3):
        for j in range(3):
            if game[i][j]=='O':
                print(Fore.RED + game[i][j] , end=' ')
            elif game[i][j]=='X':
                print(Fore.GREEN + game[i][j] , end=' ')
            else:
                print( game[i][j] , end=' ' )

        print(Fore.RESET)


def check_win():
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 'X':
            print('player 1 wins')
            exit()
        if game[0][i] == game[1][i] == game[2][i] == 'X':
            print('player 1 wins')
            exit()
        if game[0][0] == game[1][1] == game[2][2] == 'X':
            print('player 1 wins')
            exit()
        if game[0][2] == game[1][1] == game[2][0] == 'X':
            print('player 1 wins')
            exit()
    
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 'O':
            print('player 2 wins')
            exit()
        if game[0][i] == game[1][i] == game[2][i] == 'O':
            print('player 2 wins')
            exit()
        if game[0][0] == game[1][1] == game[2][2] == 'O':
            print('player 2 wins')
            exit()
        if game[0][2] == game[1][1] == game[2][0] == 'O':
            print('player 2 wins')
            exit()


game = [['-' ,'-' , '-' ],
        ['-' ,'-' , '-' ],
        ['-' ,'-' , '-' ]]

show_game()

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

