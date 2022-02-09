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
    __piecesigns = "ox"
    __piececolors = ["red", "white"]
    def __init__(self, name:str):
        self.color = CheckersPlayer.__piececolors[CheckersPlayer.__id]
        self.name = name
        self.piecesign = CheckersPlayer.__piecesigns[CheckersPlayer.__id]
        CheckersPlayer.__id += 1

    def __genpieces__(self):
        pass


class CheckersPiece:
    def __init__(self, color : str, position : tuple):
        self.color : str = color
        self.position : tuple = position


class CheckersBoard:
    def __init__(self):
        self.board : list = []

    def __gengameboard__(self, player1 : CheckersPlayer, player2 : CheckersPlayer):
        i = 0
        def genplayerrows(player : CheckersPlayer):
            while i < 3:
                row = " ".join([player.piecesign for _ in range(4)])
                row = " " + row if i%2 == 0 else row + " "
                self.board.append(row)

    def __genplayerpiece__(self, player):
        pass


class Tests(unittest.TestCase):
    def setUp(self):
        print()




if __name__ == "__main__":
    unittest.main(verbosity=2)