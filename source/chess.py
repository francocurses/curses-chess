from curses import *
from game import Game

def main(stdscr):
    initcurses(stdscr)
    game = Game(stdscr)
    game.start()

def initcurses(stdscr):
    stdscr.refresh()
    curs_set(False)
    echo()

wrapper(main)
