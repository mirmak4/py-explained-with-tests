class BoardPlayer:
    def __init__(self, name : str):
        self.name: str = name
        self.pieces = {}
        self.__gen_pieces__()

    def __gen_pieces__(self):
        pass

class BoardPiece:
    def __init__(self, color : str, position : tuple):
        self.color : str = color
        self.position : tuple = position

class Board:
    def __init__(self, player1 : BoardPlayer, player2 : BoardPlayer):
        self.board : list = []
        self.__init_gameboard__(player1, player2)

    def __init_gameboard__(self, player1: BoardPlayer, player2: BoardPlayer):
        pass
