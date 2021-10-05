'''
Main module for setting and input handling
'''

from globals import Globals
from windowhandler import WH
from pipe import MapPipe
import pipes
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
        Globals.pipe().avatar.move({'[A': Direction.Up,
                     '[B': Direction.Down,
                     '[C': Direction.Right,
                     '[D': Direction.Left}[getch() + getch()])
    elif ch_input in ('w', 'W'):
        Globals.pipe().avatar.move(Direction.Up)
    elif ch_input in ('d', 'D'):
        Globals.pipe().avatar.move(Direction.Right)
    elif ch_input in ('s', 'S'):
        Globals.pipe().avatar.move(Direction.Down)
    elif ch_input in ('a', 'A'):
        Globals.pipe().avatar.move(Direction.Left)
    elif ch_input == '\n':
        Globals.pipe().avatar()
    elif ch_input == 'Q':
        exit()
    WH.update()


if __name__ == "__main__":

    main_menu = pipes.MainMenu()
    main_menu.stack_push()
    
    UPDATE_THREAD = WH.run_loop()
    while True:
        try:
            input_handler()
            continue
        except GetchInterrupt:
            WH.update()
            
