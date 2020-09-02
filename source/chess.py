from curses import *
from player import Player
from board import Board
from prompt import Prompt
from display import Display

def main(stdscr):
    # initialize curses
    initcurses(stdscr)

    # game objects
    player1 = Player("White","♙♘♗♖♕♔")
    player2 = Player("Black","♟︎♞♝♜♛♚")
    players = [player1,player2]
    board = Board(players)
    prompt = Prompt(stdscr)
    display = Display(stdscr)

    # draw initial display
    display.drawboard(board)

    # game loop
    turn = 0
    while True:
        player = players[turn%2]
        prompt.updateplayer(player)
        move = prompt.getmove()
        report = board.applymove(player,move)
        if not report["legal"]:
            prompt.printilegal(report)
            continue
        display.drawboard(board)
        if report["win"]:
            prompt.declarewinner(player)
            display.freeze()
        turn+=1

def initcurses(stdscr):
    stdscr.refresh()
    curs_set(False)
    echo()

wrapper(main)
