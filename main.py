from windowhandler import WH
from getch import getch


from pipelements import Avatar, PipeElement
import aspects

from directions import Direction

av = Avatar((7,7))
PipeElement(aspects.Wall, (7,6))

def input_handler():
    ch = getch()
    if ch == 'w' or ch == 'W':
        av.move(Direction.Up)
    elif ch == 'd' or ch == 'D':
        av.move(Direction.Right)
    elif ch == 's' or ch == 'S':
        av.move(Direction.Down)
    elif ch == 'a' or ch == 'A':
        av.move(Direction.Left)
    WH.update()
    return

if __name__ == "__main__":
    update_process = WH.run_loop()
    while True:
        input_handler()
        continue
    pass
