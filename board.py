class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]
    
    def display(self):
        for i in range(3):
            print("|" + "|".join(self.cells[i*3:(i+1)*3]) + "|")
            if i < 2:
                print("-------")
    
    def update_cell(self, cell_no, player_symbol):
        if self.is_valid_move(cell_no):
            self.cells[cell_no - 1] = player_symbol
            return True
        return False
    
    def is_valid_move(self, cell_no):
        return 0 < cell_no <= 9 and self.cells[cell_no - 1] == " "
    
    def is_winner(self, player_symbol):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for pattern in win_patterns:
            if all(self.cells[i] == player_symbol for i in pattern):
                return True
        return False
    
    def is_tie(self):
        return all(cell != " " for cell in self.cells)
    
    def reset(self):
        self.cells = [" " for _ in range(9)]
    
    def get_board_state(self):
        board_state = ""
        for i in range(3):
            board_state += "|" + "|".join(self.cells[i*3:(i+1)*3]) + "|\n"
            if i < 2:
                board_state += "-------\n"
        return board_state
    
    def is_space_free(self, cell):
        return self.cells[cell - 1] == " "
    
    def get_copy(self):
        new_board = Board()
        new_board.cells = self.cells[:]
        return new_board
