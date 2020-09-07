from curses import *

colors = [COLOR_BLACK,
          COLOR_RED,
          COLOR_GREEN,
          COLOR_YELLOW,
          COLOR_BLUE,
          COLOR_MAGENTA,
          COLOR_CYAN,
          COLOR_WHITE]

#for color in colors:
#    print(color)

def main(stdscr):
    for i in range(1,256):
        init_pair(i,COLOR_BLACK,i)
        stdscr.addstr("TEST",color_pair(i))
    stdscr.getkey()

wrapper(main)
