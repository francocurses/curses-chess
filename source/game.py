from player import Player
from board import Board
from prompt import Prompt
from display import Display
from parser import Parser

class Game():
    def __init__(self,stdscr):
        # display objects
        self.stdscr = stdscr
        self.display = Display(self.stdscr)
        self.prompt = Prompt(stdscr)

        # game objects
        self.player1 = Player("White",u"♙♘♗♖♕♔")
        self.player2 = Player("Black",u"♟♞♝♜♛♚")
        self.players = [self.player1,self.player2]
        self.board = Board(self.players)
        self.parser = Parser()

        # game status
        self.turn = None
        self.currplayer = None # current player
        self.finish = False
        self.wplayer = None # winner player

    def start(self):
        """
        Starts the game.
        """
        self.initialize()
        while True:
            self.updateturn()
            self.performturn()
            self.checkfinish()
            if self.finish:
                break
        self.finish()

    def initialize(self):
        """
        Initialize game.
        """
        self.display.drawboard(self.board)

    def updateturn(self):
        """
        Update turn. Check for first turn 
        border case.
        """
        if self.turn is None:
            self.turn = 1
        else:
            self.turn += 1

    def performturn(self):
        """
        Performs a turn in the game.
        - Update player
        - Get the move from the current player
        - Check move validity
        - Check move legality
        - Update board with move
        """
        # update player
        cp = self.currplayer
        cp = self.players[self.turn%2]
        self.prompt.updateplayer(cp)

        # get+apply move
        while True:
            s = self.prompt.getmove()
            self.prompt.cleaninfo()
            v,m = self.parser.parsemove(s)
            if not v: # invalid move
                self.prompt.printinvalid()
                continue
            
            l = self.board.update(cp,m)
            if not l: # ilegal move
                self.prompt.printilegal()
                continue

        # display new board
        self.display.drawboard(self.board)

    def checkfinish(self):
        """
        Check for finishing conditions.
        """
        pass

    def finish(self):
        """
        Finish game.
        """
        self.prompt.finishmessage(self.wplayer)
        self.stdscr.getkey()

#    while True:
#        player = players[turn%2]
#        prompt.updateplayer(player)
#        move = prompt.getmove()
#        report = board.applymove(player,move)
#        if not report["legal"]:
#            prompt.printilegal(report)
#            continue
#        display.drawboard(board)
#        if report["win"]:
#            prompt.declarewinner(player)
#            display.freeze()
#        turn+=1
