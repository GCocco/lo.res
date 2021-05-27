from os import popen, system
from time import sleep
from threading import Thread
from pipe import Pipe
import aspects

class WH:
    size = popen("stty size").read().split()
    _rows = int(size[0])
    _cols = int(size[1])
    del(size)

    @staticmethod
    def add(row: int, col:int, obj):
        return Pipe.add(row, col, obj)

    @staticmethod
    def delete(row: int, col: int):
        return Pipe.delete(row, col)
    
    @staticmethod
    def update():
        system("clear")
        print(f"{aspects.Frame}"*int(WH._cols/2))
        for i in range(0, WH._rows-3):
            row = Pipe.get_row(i)
            k = 2
            print(f"{aspects.Frame}", end="")
            for col in row.keys():
                if col >= (WH._cols-2):
                    break
                print(f"{' '*(col-k)}{row[col]}", end="")
                k = col + 2
                pass
            print(f"{' '*(WH._cols-k-3)}{aspects.Frame}")
            pass
        print(aspects.Frame*int(WH._cols/2))
        return

    @staticmethod
    def get_size():
        return WH._rows, WH._cols


    @staticmethod
    def _win_manager_loop():
        while True:
            size = popen("stty size").read().split()
            size = int(size[0]), int(size[1])
            if size != WH.get_size():
                WH._rows= size[0]
                WH._cols = size[1]
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
