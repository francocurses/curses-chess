class Player():
    """
    A player in chess.
    """
    def __init__(self,name,attr):
        self.name = name
        self.attr = attr
        self.pieces = []
