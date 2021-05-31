'''
Contains the class handling printing and size changes on terminal
'''
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

    @staticmethod
    def set_pipe(r_pipe: 'Pipe'):
        '''
        Sets the given pipe as the one to be rendered and updated
        '''
        WH._current_pipe = r_pipe
        WH.update_size()
        WH.update()

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
        if WH._current_pipe.avatar:
            row_offset = WH._current_pipe.avatar.get_row() - int(WH._rows/2)
        else:
            row_offset = 0
        system("clear")
        if WH._current_pipe.avatar:
            print("#debug", WH._current_pipe.avatar.get_row(), WH._current_pipe.avatar.get_col()) # DEBUG
        else:
            print("#debug: no avatar") # DEBUG
        print(aspects.FRAME*WH._cols)
        for i in range(0, WH._rows-4):
            row = WH._current_pipe.get_row(i+row_offset)
            WH._printrow(row)
        print(aspects.FRAME*WH._cols)

    @staticmethod
    def _printrow(row: 'pipe.Row'):
        '''
        Prints a single Pipe Row.
        '''
        k = 2
        print(aspects.FRAME, end='')
        for col in row.keys():
            if col >= WH._cols:
                break
            if col <= 1:
                continue
            print(aspects.BLANK * (col-k) + row[col].aspect, end='')
            k = col + 1
        print(aspects.BLANK * (WH._cols-k) + aspects.FRAME)

    @staticmethod
    def _win_manager_loop():
        '''
        The loop function handling size changes of the terminal
        '''
        while True:
            if WH.update_size():
                WH.update()
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
