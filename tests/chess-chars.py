from curses import *

def main(stdscr):
    wp = "♙♘♗♖♕♔"
    bp = "♟︎♞♝♜♛♚"

    while True:
        init_pair(1,COLOR_WHITE,COLOR_BLACK)
        init_pair(2,COLOR_BLACK,COLOR_WHITE)
        stdscr.addstr(0,0,wp,color_pair(1))
        stdscr.addstr(1,0,bp,color_pair(1))
        stdscr.addstr(2,0,wp,color_pair(2))
        stdscr.addstr(3,0,bp,color_pair(2))
        init_pair(3,COLOR_WHITE,COLOR_YELLOW)
        init_pair(4,COLOR_BLACK,COLOR_YELLOW)
        stdscr.addstr(4,0,wp,color_pair(3))
        stdscr.addstr(5,0,bp,color_pair(3))
        stdscr.addstr(6,0,wp,color_pair(4))
        stdscr.addstr(7,0,bp,color_pair(4))
        init_pair(5,COLOR_WHITE,COLOR_GREEN)
        init_pair(6,COLOR_BLACK,COLOR_GREEN)
        stdscr.addstr(8,0,wp,color_pair(5))
        stdscr.addstr(9,0,bp,color_pair(5))
        stdscr.addstr(10,0,wp,color_pair(6))
        stdscr.addstr(11,0,bp,color_pair(6))
        stdscr.getkey()

wrapper(main)
