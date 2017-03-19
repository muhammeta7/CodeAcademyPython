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