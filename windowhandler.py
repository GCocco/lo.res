from os import popen, system
from time import sleep
from threading import Thread
from pipe import Pipe

import aspects


class WH:
    __COMP = 2

    _rows = 0
    _cols = 0
    
    @staticmethod
    def add(row: int, col:int, obj):
        return Pipe.add(row, col, obj)

    @staticmethod
    def delete(row: int, col: int):
        return Pipe.delete(row, col)


    @staticmethod
    def update_size() -> bool:
        sizes = popen("stty size").read().split()
        sizes = int(sizes[0]), int(int(sizes[1])/2)
        if sizes[0] == WH._rows and sizes[1] == WH._cols:
            return False
        WH._rows = sizes[0]
        WH._cols = sizes[1]
        return True
    
    @staticmethod
    def update():
        system("clear")
        print(aspects.FRAME*WH._cols)
        for i in range(0, WH._rows-4):
            row = Pipe.get_row(i)
            WH._printrow(row)
            pass
        print(aspects.FRAME*WH._cols)
        return

    @staticmethod
    def _printrow(row):
        k = 2
        print(aspects.FRAME, end='')
        for col in row.keys():
            if col > WH._cols:
                break
            print(aspects.BLANK * (col-k) + row[col].aspect, end='')
            k = col + 1
        print(aspects.BLANK*(WH._cols-k) + aspects.FRAME)
        return
    
    @staticmethod
    def _win_manager_loop():
        while True:
            if WH.update_size():
                WH.update()
                pass
            sleep(2)
            pass
        return

    @staticmethod
    def run_loop():
        WH.update()
        daem = Thread(target=WH._win_manager_loop, daemon=True)
        daem.start()
        return daem
    
    pass

