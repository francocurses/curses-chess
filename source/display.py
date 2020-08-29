from curses import *

class Display():
    """
    The guy in charge of displaying the board.
    """
    def __init__(self,stdscr):
        # display window
        self.dw = newwin(12,12,0,0)
        self.dw.box()

        # draw coordinates in window
        self.dw.addstr(1,2,"abcdefgh")
        self.dw.addstr(1,11,"abcdefgh")
        for i in range(1,8):
            self.dw.addstr(9-i, 1,str(i))
            self.dw.addstr(9-i,11,str(i))

        # board window
        self.bw = self.dw.derwin(8,8,2,2)

