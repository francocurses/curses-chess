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
        self.pw = newwin(3,COLS,12,0)
        # input text
        istr = "Input move: "
        self.pw.addstr(0,0,istr)
        # input window
        self.iw = self.pw.derwin(1,6,0,len(istr))
        # ouput windows
        self.ow1 = self.pw.derwin(1,COLS,1,0)
        self.ow2 = self.pw.derwin(1,COLS,2,0)

        # refresh windows
        self.pw.refresh()

    def updateplayer(self,player):
        """
        Update the player in the output window.
        """
        name = player.name
        self.ow1.addstr(0,0,name+"'s turn")
        self.ow1.refresh()

    def getmove(self):
        """
        Read the input from the player and
        translate it into a move object.
        """
        string = self.iw.getstr()
        string = string.decode()
        self.iw.clear()
        return string

    def cleaninfo(self):
        """
        Clean move prompt info.
        """
        self.ow2.clear()

    def printinvalid(self):
        """
        Print a message for an invalid move was
        input in the prompt.
        """
        self.ow2.addstr(0,0,"Invalid move")
        self.ow2.refresh()

    def printilegal(self):
        """
        Print a message for an ilegal move in the
        chess board.
        """
        self.ow2.addstr(0,0,"Ilegal move")
        self.ow2.refresh()
