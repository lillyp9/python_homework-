class TictactoeException(Exception):           #Remember Class defines the behavior of the object
    pass
    def __init__(self, message):
        super().__init__(message)

class Board:
    def __init__(self):
        #Initializes the game board and starting players 
        self.board_array = [["" for _ in range(3)] for _ in range(3)]   
        self.turn = "X"
        
    
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    
    def __str__(self):
      final_list = []
      for row in self.board_array:
        row_string = "|".join(row)
        final_list.append(row_string)
      output = "\n".join(final_list)
      return(output) 
    
    def move(self, move_string):
        #Processes a player's move and updates the board or raises an exception for invalid moves.
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3  # row
        column = move_index % 3  # column
        if self.board_array[row][column] != "":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"
    
    def whats_next(self):
        # Checks if the game is won, tied, or should still keep going
        #
        board = self.board_array

        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != "":
                return True, f"{row[0]} has won"

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
                return True, f"{board[0][col]} has won"

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            return True, f"{board[0][0]} has won"

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            return True, f"{board[0][2]} has won"

        # Check Cat's Game
        for row in board:
            if "" in row:
                return False, f"{self.turn}'s turn"

        
        return True, "Cat's Game"

#main() runs the program   
def main():
    board = Board()
    game_over = False

    while not game_over:
        print(board)
          

        try:
            move = input(f"{board.turn}'s move: ").strip().lower()
            board.move(move)
        except TictactoeException as e:
            print(e)
            continue

        game_over, message = board.whats_next()

       
    print(board)
    print(message)

#Starts Everything    
if __name__ == "__main__":
    main()
      
     
       
   
    
    
    
        
            
        
            
        
     