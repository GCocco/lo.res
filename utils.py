'''
Various useful functions that don't belong to other modules
'''

def _init_getch():
    try:
        from tty import setraw
        from sys import stdin
        from termios import tcgetattr, tcsetattr, TCSADRAIN

        def __getch():
            fd = stdin.fileno()
            old_settings = tcgetattr(fd)
            try:
                setraw(stdin.fileno())
                ch = stdin.read(1)
            finally:
                tcsetattr(fd, TCSADRAIN, old_settings)
                return ch

        return __getch

    except ImportError:
        from msvcrt import getch as __getch
        return __getch

getch = _init_getch()

def interr_getch(exception_class: 'class'):
    try:
        return getch()
    except exception_class:
        return None
