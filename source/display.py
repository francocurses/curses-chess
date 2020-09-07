from curses import *
import _curses

class Display():
    """
    The guy in charge of displaying the board.
    """
    def __init__(self,stdscr):
        # used colors and attributes
        init_pair(1,COLOR_WHITE,COLOR_BLACK)
        self.coo = color_pair(1)
        init_pair(2,COLOR_BLACK,COLOR_WHITE)
        self.bkg1 = color_pair(2)
        init_pair(3,COLOR_BLACK,8)
        self.bkg2 = color_pair(3)

        # display window
        self.dw = newwin(12,12,0,0)
        self.dw.box()

        # draw coordinates in window
        self.dw.addstr(1, 2,"abcdefgh",self.coo)
        self.dw.addstr(10,2,"abcdefgh",self.coo)
        for i in range(1,9):
            self.dw.addstr(10-i, 1,str(i),self.coo)
            self.dw.addstr(10-i,10,str(i),self.coo)

        # board window
        self.bw = self.dw.derwin(8,8,2,2)

        # refresh display
        self.dw.refresh()

    def drawboard(self,board):
        """
        Draw the given board in its current state
        in the board window.
        """
        m = board.matrix # board matrix
        (cols, rows) = m.shape
        for y in range(cols):
            for x in range(rows):
                piece = m[y,x]
                self.drawpiece(piece,y,x)
        self.bw.refresh()

    def drawpiece(self,piece,y,x):
        """
        Draw a chess piece in the board. If piece
        is None, then draw nothing.
        """
        # choose color depending in position
        color = self.bkg1 if (x+y)%2 else self.bkg2
    
        # draw piece character
        char = " "
        if piece is not None:
            char = piece.char
        addstr(self.bw,y,x,char,color)

def addstr(w,y,x,s,a=A_NORMAL):
    """
    Add string s into window w at position (y,x)
    safetely, meaning you won't deal with the
    curses error in the bottom right corner
    """
    try:
        w.addstr(y,x,s,a)
    except _curses.error as e:
        pass
