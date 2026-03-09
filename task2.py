board = [" "] * 9

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

print("Tic Tac Toe Game")

for turn in range(9):
    print_board()
    move = int(input("Enter position (0-8): "))

    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move")
        continue

    if check_win("X"):
        print_board()
        print("You Win!")
        break
else:
    print("Game Draw")