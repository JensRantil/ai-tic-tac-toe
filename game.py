from board import Board
from player import Player

class Game:
    def __init__(self, player_x=None, player_o=None):
        self.board = Board()
        self.player_X = player_x if player_x else Player("X")
        self.player_O = player_o if player_o else Player("O")
        self.current_player = self.player_X

    def switch_player(self):
        if self.current_player == self.player_X:
            self.current_player = self.player_O
        else:
            self.current_player = self.player_X

    def play(self):
        while True:
            self.current_player.make_move(self.board)
            self.board.display()
            if self.board.is_winner(self.current_player.symbol):
                self.board.display()
                print(f"Player {self.current_player.symbol} wins!")
                break
            elif self.board.is_tie():
                self.board.display()
                print("It's a tie!")
                break
            else:
                self.switch_player()

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.board.reset()
            self.play()
