from curses import *

class Prompt():
    """
    Game prompt for receiving inputs and
    displaying messages.
    """
    def __init__(self,stdscr):
        # get screen size
        (ROWS,COLS) = stdscr.getmaxyx()

        # define prompt windows:
        # prompt window
        self.pw = newwin(3,COLS,10,0)
        # input text
        istr = "Input move: "
        self.pw.addstr(0,0,istr)
        # input window
        self.iw = self.pw.derwin(1,2,0,len(istr))
        # ouput windows
        self.ow1 = self.pw.derwin(1,COLS,1,0)
        self.ow2 = self.pw.derwin(1,COLS,2,0)

    def getmove(self):
        """
        Read the input from the player.
        """
        return None
