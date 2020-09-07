class Parser():
    """
    This guy parses a move in algebraic notation
    and convert it i to a Move objects. It also
    report if the move is valid or not.
    """
    def __init__(self):
        self.cols = "abcdefgh"
        self.rows = "12345678"

    def parsemove(self,s):
        """
        Parses a move s in string format and 
        return a dictionary that reports if the
        move is valid, and a move object.
        """
        # case 2 chars
        if len(s)==2:
            r = self.parse_2charsmove(s)
        # case 3 chars
        elif len(s)==3:
            r = self.parse_3charsmove(s)
        # case 4 chars
        elif len(s)==4:
            r = self.parse_4charsmove(s)
        # case 5 chars
        elif len(s)==5:
            r = self.parse_5charsmove(s)
        # case too few characters
        else:
            r = genirep("Too few characters")

        return r

    def parse_2charsmove(self,s):
        """
        Parse two characters move. Cases:
        - pawn non-promotion move
        """
        iscoor,y,x = self.check_coor(s)
        if iscoor:
            return genmove(Pawn,y,x)
        return genirep("Invalid move")

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
            return genmove(piece,y,x)
        ismove,yf,xf,xi = self.check_pawnd_move(s)
        if ismove:
            return genmove(Pawn,yf,xf,xi=xi)
        return genirep("Invalid move")

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
        y = ord(s)-97
        return iscol,y

    def check_row(self,s):
        isrow = s in self.rows
        x = int(s)
        return isrow,x

def genireport(info):
    """
    Generate an invalid report with an info
    message.
    """
    r["valid"] = False
    r["info"] = info
    return r

def genmove(piece,yf,xf,yi=None,xi=None):
    """
    Generate a move given a piece, an its
    coordinates.
    """
    r["valid"] = True
    r["move"] = Move(piece,yf,xf,yi,xi)
    return r

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

