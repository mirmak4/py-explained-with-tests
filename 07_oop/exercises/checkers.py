import logging
import random
import unittest

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)7s %(asctime)s [%(filename)13s:%(lineno)4d] %(message)s",
)

log = logging.getLogger()


class CheckersPlayer:
    __id = 0
    __piece_signs = "ox"
    __piece_colors = ["red", "white"]
    __pieces_row_nr = 0
    def __init__(self, name:str):
        self.color : str = CheckersPlayer.__piece_colors[CheckersPlayer.__id]
        self.name : str = name
        self.piecesign : str = CheckersPlayer.__piece_signs[CheckersPlayer.__id]
        self.pieces = {}
        CheckersPlayer.__id += 1
        self.__gen_pieces__()

    def __gen_pieces__(self):
        # 3 rows of checkers for each player
        pos_y = CheckersPlayer.__pieces_row_nr
        player_row_count = pos_y + 3
        while pos_y < player_row_count:
            even_y = 1 if pos_y%2 == 0 else 0
            for x in range(4):
                pos_x = x * 2 + even_y
                pos = (pos_x, pos_y)
                piece = CheckersPiece(self.color, pos)
                self.pieces[pos] = piece
            pos_y += 1
        # move row pointer: 3 rows of checkrs + 2 empty rows in the middle of board
        CheckersPlayer.__pieces_row_nr += 5


class CheckersPiece:
    def __init__(self, color : str, position : tuple):
        self.color : str = color
        self.position : tuple = position


class CheckersBoard:
    def __init__(self, player1 : CheckersPlayer, player2 : CheckersPlayer):
        self.board : list = []
        self.__init_gameboard__(player1, player2)

    def __init_gameboard__(self, player1 : CheckersPlayer, player2 : CheckersPlayer):
        row_nr = 0
        def init_player_rows(player : CheckersPlayer):
            nonlocal row_nr
            row : str = " " if row_nr%2 == 0 else ""
            for i in range(1, len(player.pieces)+1):
                row += player.piecesign + " "
                if i%4 == 0:
                    row = row[:-1] if row_nr%2 == 0 else row
                    self.board.append(row)
                    row_nr += 1
                    row = " " if row_nr % 2 == 0 else ""

        init_player_rows(player1)
        self.board.append(" "*8)
        self.board.append(" " * 8)
        init_player_rows(player2)

    def __repr__(self):
        board_str : str = ""
        for row in self.board:
            board_str += row + "\n"
        return board_str


class Tests(unittest.TestCase):
    def setUp(self):
        print()

    def test_game(self):
        player1 = CheckersPlayer(input("Type name for first player: "))
        player2 = CheckersPlayer(input("Type name for second player: "))
        game_board = CheckersBoard(player1, player2)
        print(game_board)
        self.assertEqual(8, len(game_board.board))
        for x in range(len(game_board.board)):
            self.assertEqual(8, len(game_board.board[x]))


if __name__ == "__main__":
    unittest.main(verbosity=2)