from pieces.pawn import Pawn
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King

class Parser():
    """
    This guy parses a move in algebraic notation
    and convert it i to a Move objects. It also
    report if the move is valid or not.
    """
    def __init__(self):
        self.cols = "abcdefgh"
        self.rows = "12345678"
        self.pdict = {"N" : Knight,
                      "B" : Bishop,
                      "R" : Rook,
                      "Q" : Queen,
                      "K" : King}

    def parsemove(self,s):
        """
        Parses a move s in string format and 
        return a dictionary that reports if the
        move is valid, and a move object.
        """
        # case 2 chars
        if len(s)==2:
            v,move = self.parse_2charsmove(s)
        # case 3 chars
        elif len(s)==3:
            v,move = self.parse_3charsmove(s)
        # case 4 chars
        elif len(s)==4:
            v,move = self.parse_4charsmove(s)
        # case 5 chars
        elif len(s)==5:
            v,move = self.parse_5charsmove(s)
        # case too few characters
        else:
            return False,None

        return v,move

    def parse_2charsmove(self,s):
        """
        Parse two characters move. Cases:
        - pawn non-promotion move
        """
        iscoor,y,x = self.check_coor(s)
        if not iscoor:
            return genmove(Pawn,y,x)
        return False,None

    def parse_3charsmove(self,s):
        """
        Parse 3 characters move. Cases:
        - main piece move
        - pawn diambiguation move
        - pawn promotion move
        - king side castle
        """
        ismove,p,y,x = self.check_mpiece_move(s)
        if ismove:
            return genmove(p,y,x)
        ismove,yf,xf,xi = self.check_pawnd_move(s)
        if ismove:
            return genmove(Pawn,yf,xf,xi=xi)
        return False,None

    def check_coor(self,s):
        """
        Check if string s represents a coordinate.
        Return false if not. Return the board
        coordinates if true.
        """
        iscol,y = self.check_col(s[0])
        isrow,x = self.check_row(s[1])
        iscoor = iscol&isrow
        return iscoor,y,x

    def check_col(self,s):
        iscol = s in self.cols
        if iscol:
            y = ord(s)-97
            return iscol,y
        return False,None

    def check_row(self,s):
        isrow = s in self.rows
        if isrow:
            x = int(s)
            return isrow,x
        return False,None

    def check_mpiece_move(self,s):
        """
        Check if string is a move from a main
        piece. Return false if not. Return
        piece class and coordinates if true.
        """
        if s[0] not in self.pdict.keys():
            return False,None,None,None
        p = self.pdict[s[0]]
        iscoor,y,x = self.check_coor(s[1:])
        if not iscoor:
            return False,None,None,None
        return True,p,y,x

def genmove(piece,yf,xf,yi=None,xi=None):
    """
    Generate a move given a piece, an its
    coordinates.
    """
    return True, Move(piece,yf,xf,yi,xi)

class Move():
    """
    A move parsed from string in algebraic 
    notation.
    """
    def __init__(self,piece,yf,xf,yi=None,xi=None):
        self.piece = piece
        self.yf = yf
        self.xf = xf
        self.yi = yi
        self.xi = xi

