import numpy as np

class Board():
    """
    The chessboard.
    """
    def __init__(self,players):
        self.matrix = np.empty((8,8),object)
        
        # add chess pieces
        self.add_chesspieces(0,players[0])
        self.add_chesspieces(1,players[1])

    def add_chesspieces(self,n,player):
        """
        Add chess pieces to the board.
        """
        poss = getposs(n)
        pieces = player.pieces
        for pos, piece in zip(poss,pieces):
            self.matrix[pos.y,pos.x] = piece

    def applymove(self,player,move):
        """
        Apply the input move into the board.
        Invalid moves do nothing. The results
        of the move are returned in report
        dictionary.
        """
        # init empty report
        global report
        report = {}

        # check move legality
        self.legalizemove(player,move)

        # update board with move
        if report["legal"]:
            self.update(move,report)
        
        return report
    
    def legalizemove(self,player,move):
        """
        Check if move is a legal move for the
        player.
        """
        # TODO
        global report
        report["legal"] = False

def getposs(n):
    """
    Get initial pieces positions for player
    number n.
    """
    if n==0: # whites
        prow = 6 # pawns row
        mrow = 7 # main pieces row
    elif n==1: # blacks
        prow = 1 # pawn row
        mrow = 0 # main pieces row

    pposs = [] # pawn positions
    mposs = [] # main pieces positions
    for i in range(8):
        pposs.append(Pos(prow,i))
        mposs.append(Pos(mrow,i))

    return pposs + mposs

class Pos():
    """
    A position of a chess piece in the board.
    """
    def __init__(self,y,x):
        self.y = y
        self.x = x
