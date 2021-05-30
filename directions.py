'''
Just a module containing an enum to ease directions
'''
from enum import IntEnum

class Direction(IntEnum):
    '''
    An enumeration of direction as integer
    '''
    Up = 1
    Right = 2
    Down = 4
    Left = 8
