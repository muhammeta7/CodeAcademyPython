# Battleship

## Make a list
board=[]
    
for i in range(0, 5):
    board.append(['O'] * 5)
print(board)

## Custom Print
board=[]
    
for i in range(0, 5):
    board.append(['O'] * 5)
## Within function create for loop to iterate through each row and print
def print_board(board):
    for row in board:
        print row

print_board(board)

## Print pretty without []
board=[]
    
for i in range(0, 5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

## Create random row and column
from random import randint

def random_row(board):
    return randint(0, len(board)-1)
    
def random_col(board):
    return randint(0, len(board)-1)
    
ship_row = random_row(board)
ship_col = random_col(board)
print ship_col # Debugging purposes
print ship_row

## Allow user to guess
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Conditional to check if you win
for turn in range(4):
  print "Turn", turn+1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sank my battleship!"
  else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      if guess_row not in range(5) or \
          guess_col not in range(5):
              print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == "X":
          print "You guessed that one already."
          turn = turn + 1
      else:
          print "You missed my battleship!"
          board[guess_row][guess_col]="X"
          if turn == 3:
            print "Game Over"
      
      print_board(board)
          
