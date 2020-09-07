from curses import *
from parser import Parser

class Prompt():
    """
    Game prompt for receiving inputs and
    displaying messages.
    """
    def __init__(self,stdscr):
        # get screen size
        (ROWS,COLS) = stdscr.getmaxyx()
        
        # create move parser
        self.parser = Parser()

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
        while True:
            s = self.iw.getstr()
            s = decode()
            self.iw.clear()
            report = self.parser.parsemove(s)
            if report["valid"]:
                break
            self.ow2.addstr(0,0,"Invalid move")
            self.ow2.refresh()
        return report["move"]

    def printilegal(self,report):
        """
        Print a message for an ilegal move in the
        chess board.
        """
        self.ow2.addstr(0,0,"Ilegal move")
        self.ow2.refresh()

def parsemove(s):
    """
    Transtale a string into a Move object that
    the chess board can uae to update the game.
    It return valid=False if the move can not
    be parsed.
    """
    report = {"valid" : False}
    return report
