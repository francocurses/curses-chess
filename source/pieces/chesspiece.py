class ChessPiece():
    """
    Generic chess piece.
    """
    def __init__(self,char):
        self.char = char
        self.y = None
        self.x = None

    def place(self,y,x):
        """
        Update the piece position information
        (doesn't actually move the piece in
        the board).
        """
        self.y = y
        self.x = x
