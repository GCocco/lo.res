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
        sizes = int(sizes[0])-WH.__COMP, int(sizes[1])-WH.__COMP
        if sizes[0] == WH._rows and sizes[1] == WH._cols:
            return False
        WH._rows = sizes[0]
        WH._cols = sizes[1]
        return True
    
    @staticmethod
    def update():
        system("clear")
        print(aspects.Frame*int(WH._cols/WH.__COMP))
        for i in range(0, WH._rows-4):
            row = Pipe.get_row(i)
            WH._printrow(row)
            pass
        print(aspects.Frame*int(WH._cols/WH.__COMP))
        return

    @staticmethod
    def _printrow(row):
        k = WH.__COMP
        print(aspects.Frame, end='')
        for col in row.keys():
            if col > WH._cols:
                break
            print(aspects.Blank*int((col-k)/WH.__COMP) + row[col], end='')
            k = col + WH.__COMP
        print(aspects.Blank*int((WH._cols-k)/WH.__COMP) + aspects.Frame)
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
        daem.run()
        return daem
    
    pass


#DEBUG ZONE
#TODO: CANCELLARE QUESTA ROBA

Pipe.add(5, 5, aspects.Wall)
Pipe.add(5, 6, aspects.Wall)
Pipe.add(5, 10, aspects.Wall)
Pipe.add(10, 10, aspects.Wall)
Pipe.add(7, 50, aspects.Wall)
