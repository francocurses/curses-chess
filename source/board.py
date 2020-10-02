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

    def update(self,player,move):
        """
        Apply the input move into the board.
        Invalid moves do nothing, and a false
        value is returned.
        """
        # check move legality
        legal,move = self.legalizemove(player,move)

        # update board with move
        if legal:
            self.applymove(move)
        
        return legal
    
    def legalizemove(self,player,move):
        """
        Check if move is a legal move for the
        player. Steps:
        - get the piece type
        - get the individual piece
        - check if the piece can move to the
            desired destination
        """
        plist = identifypiece(player,move.pclass)
        #TODO: get individual piece
        move.piece = plist[0]
        #TODO: check move validity
        
        return True,move

    def applymove(self,move):
        """
        Apply the move in the board.
        """
        self.removepiece(move.capture)
        self.movepiece(move)
        self.promotepiece(move)

    def removepiece(self,move):
        """
        Remove a piece from the board.
        Used  when a piece is captured.
        """
        # remove piece from board
        y = move.capture.y
        x = move.capture.x
        self.matrix[y,x] = None

        # remove piece from player list


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

def identifypiece(player,pc):
    """
    Return the piece list or piece from player
    given piece class pc.
    """
    if pc is Pawn:
        return player.pawns
    if pc is Knight
        return player.knights
    if pc is Bishop:
        return player.bishops
    if pc is Queen:
        return [player.queen]
    if pc is King:
        return [player.king]
    return None

class Pos():
    """
    A position of a chess piece in the board.
    """
    def __init__(self,y,x):
        self.y = y
        self.x = x
