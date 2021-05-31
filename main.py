'''
Main module for setting and input handling
'''
from windowhandler import WH
from pipe import Pipe
from getch import getch

from pipelements import Avatar, PipeElement
import aspects

from directions import Direction

MAP_PIPE = Pipe()
WH.set_pipe(MAP_PIPE)
AVATAR = Avatar(MAP_PIPE, (7, 7))
PipeElement(MAP_PIPE, aspects.TREE, (7, 6))

def input_handler():
    '''
    waits for a input and processes it
    '''
    ch_input: str = getch()
    if ch_input in ('w', 'W'):
        AVATAR.move(Direction.Up)
    elif ch_input in ('d', 'D'):
        AVATAR.move(Direction.Right)
    elif ch_input in ('s', 'S'):
        AVATAR.move(Direction.Down)
    elif ch_input in ('a', 'A'):
        AVATAR.move(Direction.Left)
    WH.update()

if __name__ == "__main__":
    UPDATE_THREAD = WH.run_loop()
    while True:
        input_handler()
        continue
