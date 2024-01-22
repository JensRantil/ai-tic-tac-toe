import openai
from game import Game
import random

class GPTPlayer:
    def __init__(self, token):
        self.token = token
        self.symbol = 'X'
        openai.api_key = self.token

    def make_move(self, board):
        prompt = board.get_board_state() + "\nYou are player X in a game of TicTacToe. It's your turn. What is the best move given this board? You can't put your marker on a preexisting place."
        response = openai.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "You are an assistant responding with an integer between 1-9 with no additional context or description."},
                #{"role": "system", "content": "You are professional TicTacToe player responding with an integer between 1-9 with additional context or description."},
                {"role": "user", "content": prompt}
          ]
        )
        print(response)
        content = response.choices[0].message.content.strip()
        print("Response:", content)
        board.update_cell(int(content), self)


class RuleBasedPlayer:
    def __init__(self):
        self.symbol = 'X'

    def make_move(self, board):
        board.update_cell(self._pick_move(board), self.symbol)

    def _pick_move(self, board):
        # Check if we can win in the next move
        for i in range(1, 10):
            copy = board.get_copy()
            if copy.is_space_free(i):
                copy.update_cell(i, self.symbol)
                if copy.is_winner(self.symbol):
                    return i

        # Check if the opponent can win in the next move and block them
        for i in range(1, 10):
            copy = board.get_copy()
            if copy.is_space_free(i):
                copy.update_cell(i, 'O')  # Assuming the opponent is 'O'
                if copy.is_winner('O'):
                    return i

        # Try to take one of the corners, if they are free.
        move = self._choose_random_move_from_list(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if board.is_space_free(5):
            return 5

        # Move on one of the sides.
        return self._choose_random_move_from_list(board, [2, 4, 6, 8])

    def _choose_random_move_from_list(self, board, moves_list):
        possible_moves = []
        for i in moves_list:
            if board.is_space_free(i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None


def main():
    #player_x = GPTPlayer("CHATGPT API KEY")
    player_x = RuleBasedPlayer()
    game = Game(player_x=player_x)
    game.play()

if __name__ == "__main__":
    main()
