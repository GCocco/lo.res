from windowhandler import WH
from threading import Thread
from getch import getch
import aspects


WH.add(6, 10, aspects.Avatar)

def input_handler_loop():
    while True:
        ch = getch()
        if ch == 'a' or ch == 'A':
            pass
        pass
    return

if __name__ == "__main__":
    WH.run_loop()
    pass
