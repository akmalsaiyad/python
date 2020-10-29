from os import system
import time

#all the methods
global toss
global tictactoe_string
global tictactoe_values

toss = 1
tictactoe_string =' ___..___..___\n|_{}_||_{}_||_{}_|\n|_{}_||_{}_||_{}_|\n|_{}_||_{}_||_{}_|'
tictactoe_values = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def display_tictactoe():
       global tictactoe_string
       global tictactoe_values
       print(tictactoe_string.format(tictactoe_values[0],tictactoe_values[1],tictactoe_values[2],tictactoe_values[3],tictactoe_values[4],tictactoe_values[5],tictactoe_values[6],tictactoe_values[7],tictactoe_values[8]))
  
def action():
       global toss
       system('cls')
       display_tictactoe()

       position = int(input('\nplayer {}- enter a digit from num pad: '.format(toss)))
       flag = check_empty(position-1)


       if(flag):
              if toss == 1:
                     setplayer(position-1,toss)
                     
              if toss == 2:
                     setplayer(position-1,toss)

                     
       else:
              print('Please fill the empty ones\nPress any single keys from 1 to 9\nPress Enter to continue')
              input()
              action()

def setplayer(position,num):
       global tictactoe_values
       global toss
       if num == 1:
              tictactoe_values[position] = 'X'
              toss = 2
              check_status()
              action()
       if num == 2:
              tictactoe_values[position] = '0'
              toss = 1
              check_status()
              action()
def check_empty(pos):
       global tictactoe_values
       if pos > 8 or pos < 0:
              return False
       if tictactoe_values[pos] == ' ':
              return True
       else:
              return False

def check_status():
       global tictactoe_values
       for i in range(0,9,3):
              if  tictactoe_values[i] ==  tictactoe_values[i+1] == tictactoe_values[i+2] != ' ':
                     if tictactoe_values[i] == 'X':
                            system('cls')
                            display_tictactoe()
                            print('\n\nWinner - Player 1\n\n')
                            reset()
                     if tictactoe_values[i] == '0':
                            system('cls')
                            display_tictactoe()
                            print('\n\nWinner - Player 2\n\n')
                            reset()
       for i in range(3):
              if  tictactoe_values[i] ==  tictactoe_values[i+3] == tictactoe_values[i+6] != ' ':
                     if tictactoe_values[i] == 'X':
                            system('cls')
                            display_tictactoe()
                            print('\n\nWinner - Player 1\n\n')
                            reset()
                     if tictactoe_values[i] == '0':
                            system('cls')
                            display_tictactoe()
                            print('\n\nWinner - Player 2\n\n')
                            reset()
       
       if  tictactoe_values[0] ==  tictactoe_values[4] == tictactoe_values[8] != ' ':
              if tictactoe_values[0] == 'X':
                     system('cls')
                     display_tictactoe()
                     print('\n\nWinner - Player 1\n\n')
                     reset()
              if tictactoe_values[0] == '0':
                     system('cls')
                     display_tictactoe()
                     print('\n\nWinner - Player 2\n\n')
                     reset()

       if  tictactoe_values[2] ==  tictactoe_values[4] == tictactoe_values[6] != ' ':
              if tictactoe_values[2] == 'X':
                     system('cls')
                     display_tictactoe()
                     print('\n\nWinner - Player 1\n\n')
                     reset()
              if tictactoe_values[2] == '0':
                     system('cls')
                     display_tictactoe()
                     print('\n\nWinner - Player 2\n\n')
                     reset()

       if not ' ' in tictactoe_values:
              system('cls')
              display_tictactoe()
              print('\n\nMatch Draw\n\n')
              reset()
       
def reset():
       global toss
       global tictactoe_string
       global tictactoe_values
       while True:
              try:
                     ii = int(input("Do you wish to play again?\nenter '1' to continue or enter '0' to exit\n"))
              except:
                     print('\nWrong input!!!\n')
                     continue

              if ii == 1:
                     toss = 1
                     tictactoe_values = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
                     action()
              elif ii == 0:
                     exit()
              else:
                     print('\nWrong input!!!\n')
              


# start of program
system('cls')
print('''\n\n\t\t\tTIC TAC TOE

       
keypad    ___  ___  ___                  ___  ___  ___
         |_1_||_2_||_3_|                |_X_||_0_||_X_|
         |_4_||_5_||_6_|        ==>>    |_0_||_X_||_0_|    [here X and 0 are just for demo]
         |_7_||_8_||_9_|                |_X_||_0_||_X_|

player 1 - ' X '
player 2 - ' 0 '
choose among yourself who will be player 1 and player 2
first chance will be of player 1

press 'Enter' when you are ready
''')
key = input()
action()
