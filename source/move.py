class Move():
    """
    A move from a chess player. Note: castling
    ia represented as two moves.
    """
    def __init__(self,pclass,
            yi=None,
            xi=None,
            yf=None,
            xf=None,
            promote=None):
        self.pclass = pclass
        self.piece = None
        self.yi = yi
        self.xi = xi
        self.yf = yf
        self.xf = xf
        self.capture = None
        self.promote = promote

