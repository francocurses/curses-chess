from curses import *
from player import Player
from board import Board
from prompt import Prompt
from display import Display

def main(stdscr):
    # initialize curses
    initcurses(stdscr)

    # game objects
    player1 = Player("White",A_NORMAL)
    player2 = Player("Black",A_DIM)
    players = [player1,player2]
    board = Board(players)
    prompt = Prompt(stdscr)
    display = Display(stdscr)

    # game loop
    turn = 0
    while True:
        player = players[turn%2]
        move = prompt.getmove()
        valid,win = board.applymove(player,move)
        if not valid:
            prompt.printinvalid()
            continue
        display.drawboard(board)
        if win:
            prompt.declarewinner(player)
            display.freeze()
        turn+=1

def initcurses(stdscr):
    stdscr.refresh()
    curs_set(False)
    echo()

wrapper(main)
