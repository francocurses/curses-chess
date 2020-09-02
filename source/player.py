from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King

class Player():
    """
    A player in chess.
    """
    def __init__(self,name,pstring):
        self.name = name
        self.getpchars(pstring)

        # create chess pieces
        # pawns
        self.pawns = []
        for _ in range(8):
            self.pawns.append(Pawn(self.pchar))
        # knights
        self.knight1 = Knight(self.nchar)
        self.knight2 = Knight(self.nchar)
        self.knights = [self.knight1,self.knight2]
        # bishops
        self.bishop1 = Bishop(self.bchar)
        self.bishop2 = Bishop(self.bchar)
        self.bishops = [self.bishop1,self.bishop2]
        # rooks
        self.rook1 = Rook(self.rchar)
        self.rook2 = Rook(self.rchar)
        self.rooks = [self.rook1,self.rook2]
        self.queen = Queen(self.qchar)
        self.king = King(self.kchar)

        # add pieces in "read" order
        self.pieces = self.pawns + [self.rook1] + \
            [self.knight1] + [self.bishop1] + \
            [self.queen] + [self.king] + \
            [self.bishop2] + [self.knight2] + \
            [self.rook2]

    def getpchars(self,pstring):
        """
        Separates every character of the pieces
        string and creates an attribute with each.
        """
        self.pchar = pstring[0]
        self.nchar = pstring[1]
        self.bchar = pstring[2]
        self.rchar = pstring[3]
        self.qchar = pstring[4]
        self.kchar = pstring[5]

