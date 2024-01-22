class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                cell_no = int(input(f"Player {self.symbol}, enter your move (1-9): "))
                if board.update_cell(cell_no, self.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
