def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Enter moves using numbers 1-9 (left to right, top to bottom)")
    print("Example board with positions:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("\nLet's begin!\n")
    
    while True:
        print_board(board)
        print(f"\nPlayer {current_player}'s turn")
        
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if 0 <= move <= 8:
                    row = move // 3
                    col = move % 3
                    if board[row][col] == " ":
                        break
                    else:
                        print("That position is already taken!")
                else:
                    print("Please enter a number between 1 and 9!")
            except ValueError:
                print("Please enter a valid number!")
        
        board[row][col] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"\nPlayer {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("\nIt's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main() 