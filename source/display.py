from curses import *
import _curses

class Display():
    """
    The guy in charge of displaying the board.
    """
    def __init__(self,stdscr):
        # used colors
        init_pair(1,COLOR_RED,COLOR_BLACK)
        red = color_pair(1)


        # display window
        self.dw = newwin(12,12,0,0)
        self.dw.box()

        # draw coordinates in window
        self.dw.addstr(1, 2,"abcdefgh",red)
        self.dw.addstr(10,2,"abcdefgh",red)
        for i in range(1,9):
            self.dw.addstr(10-i, 1,str(i),red)
            self.dw.addstr(10-i,10,str(i),red)

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
                if piece is None:
                    addstr(self.bw,y,x,"X")
                else:
                    c = piece.char
                    addstr(self.bw,y,x,c)
        self.bw.refresh()

def addstr(w,y,x,s):
    """
    Add string s into window w at position (y,x)
    safetely, meaning you won't deal with the
    curses error in the bottom right corner
    """
    try:
        w.addstr(y,x,s)
    except _curses.error as e:
        pass
