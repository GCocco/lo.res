from os import popen, system
from time import sleep
from threading import Thread
from pipe import Pipe

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
        print("#"*WH._cols)
        for i in range(0, WH._rows-3):
            print(f'#{" "*(WH._cols-2)}#')
            pass
        print("#"*WH._cols)
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

Pipe.add(5, 5, "Y")
