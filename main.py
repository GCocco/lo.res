'''
Main module for setting and input handling
'''
from windowhandler import WH
from pipe import Pipe
from getch import getch

import pipelements
import aspects

from directions import Direction
from structures import TreeBox

# DEBUG/TEST stuff
MAP_PIPE = Pipe()
WH.set_pipe(MAP_PIPE)
AVATAR = pipelements.Avatar(MAP_PIPE, (7, 7))
pipelements.PipeElement(MAP_PIPE, aspects.WALL, (7, 6))
pipelements.Tree(MAP_PIPE, (8, 7))
pipelements.from_string('Tree')(MAP_PIPE, (8, 9))

TreeBox(MAP_PIPE, (10, 10))

# end DEBUG/TEST stuff

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
