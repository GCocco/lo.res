'''
Main module for setting and input handling
'''
from globals import Globals
from windowhandler import WH
from pipe import MapPipe
from getch import getch



import pipelements
import aspects
import signal

from directions import Direction
from structures import PipeTreeBox, PipeText
from time import sleep
from threading import Thread
from exceptions import GetchInterrupt
import dialogpipe
# DEBUG/TEST stuff
if False:
    MAP_PIPE = MapPipe()
    WH.set_pipe(MAP_PIPE)
    Globals.stack().push(MAP_PIPE)
    AVATAR = pipelements.Avatar(MAP_PIPE, (7, 7))
    pipelements.PipeElement(MAP_PIPE, aspects.WALL, (7, 6))
    pipelements.Tree(MAP_PIPE, (8, 7))
    pipelements.from_string('Tree')(MAP_PIPE, (8, 9))

    PipeTreeBox(MAP_PIPE, (10, 10))
    TEST_INTERACTABLE = pipelements.Interactable(MAP_PIPE, aspects.SKULL, (4, 4))
    TEST_INTERACTABLE.set_function(TEST_INTERACTABLE.delete)
    pass
else:
    D_PIPE = dialogpipe.DialogPipe("Menu")
    WH.set_pipe(D_PIPE)
    Globals.stack().push(D_PIPE)
    dialogpipe.DialogButton(D_PIPE, "opt1")
    dialogpipe.DialogButton(D_PIPE, "opt2")
    dialogpipe.DialogButton(D_PIPE, "opt3")
    dialogpipe.DialogButton(D_PIPE, "opt4")
    dialogpipe.DialogButton(D_PIPE, "opt5")
    dialogpipe.DialogButton(D_PIPE, "opt6")
    dialogpipe.DialogButton(D_PIPE, "opt7")
    dialogpipe.DialogButton(D_PIPE, "opt8")
    dialogpipe.DialogButton(D_PIPE, "opt9")
    dialogpipe.DialogButton(D_PIPE, "opt10")
    dialogpipe.DialogButton(D_PIPE, "opt11")
    dialogpipe.DialogButton(D_PIPE, "opt12")
    dialogpipe.DialogButton(D_PIPE, "opt13")
    dialogpipe.DialogButton(D_PIPE, "opt14")
    dialogpipe.DialogButton(D_PIPE, "opt15")
    dialogpipe.DialogButton(D_PIPE, "opt16")
    dialogpipe.DialogButton(D_PIPE, "opt17")
    dialogpipe.DialogButton(D_PIPE, "opt18")
    dialogpipe.DialogButton(D_PIPE, "opt19")
    dialogpipe.DialogButton(D_PIPE, "opt20")
    dialogpipe.DialogButton(D_PIPE, "opt21")
    AVATAR = D_PIPE.avatar
# end DEBUG/TEST stuff


def input_handler():
    '''
    waits for a input and processes it
    '''

    def interrupt_func(signum, frame):
        raise GetchInterrupt()

    signal.signal(signal.SIGALRM, interrupt_func)
    signal.alarm(3)
    try:
        ch_input: str = getch()
    except OverflowError:
        return
    signal.alarm(0)
    if ch_input == '\x1b':
        AVATAR.move({'[A': Direction.Up,
                     '[B': Direction.Down,
                     '[C': Direction.Right,
                     '[D': Direction.Left}[getch() + getch()])
    elif ch_input in ('w', 'W'):
        AVATAR.move(Direction.Up)
    elif ch_input in ('d', 'D'):
        AVATAR.move(Direction.Right)
    elif ch_input in ('s', 'S'):
        AVATAR.move(Direction.Down)
    elif ch_input in ('a', 'A'):
        AVATAR.move(Direction.Left)
    elif ch_input == '\n':
        AVATAR()
    elif ch_input == 'Q':
        exit()
    WH.update()


if __name__ == "__main__":
    UPDATE_THREAD = WH.run_loop()
    while True:
        try:
            input_handler()
            continue
        except GetchInterrupt:
            WH.update()
            
