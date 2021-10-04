'''
Contains the class handling printing and size changes on terminal
'''
from globals import Globals

from os import popen, system
from time import sleep
from threading import Thread
import aspects


class WH:
    '''
    Used for printing and handling size changes
    '''
    _rows = 0
    _cols = 0
    _current_pipe = None
    update_flag = False


    @staticmethod
    def update_size() -> bool:
        '''
        Checks if size of terminal has changed. If it has, updates the info and returns True.
        '''
        sizes = popen("stty size").read().split()
        sizes = int(sizes[0]), int(int(sizes[1])/2)
        if sizes[0] == WH._rows and sizes[1] == WH._cols:
            return False
        WH._rows = sizes[0]
        WH._cols = sizes[1]
        return True

    @staticmethod
    def update():
        '''
        Flushes and prints the pipe.
        '''
        WH.update_flag = False
        system("clear")
        Globals.pipe().print((WH._rows-4, WH._cols))

    @staticmethod
    def _win_manager_loop():
        '''
        The loop function handling size changes of the terminal
        '''
        while True:
            if WH.update_size():
                WH.update_flag = True
            sleep(2)

    @staticmethod
    def run_loop() -> 'Thread':
        '''
        Runs the win_manager_loop as a daemon thread and returns it.
        '''
        WH.update()
        daem = Thread(target=WH._win_manager_loop, daemon=True)
        daem.start()
        return daem
