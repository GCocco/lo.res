'''
This module contains various Exceptions
'''

class OccupiedSpaceError(Exception):
    '''
    A error raised when attempting to add a pipelement in a occupied slot.
    '''
    def __init__(self, pipe, row, col):
        '''
        Constructor
        '''
        super().__init__(f"space in {row, col} occupied")
        self.lmnt = pipe.get(row, col)


class PrioritySignal(Exception):
    '''
    An exception to be used for interrupting a blocking call such as getch()
    '''
    def __init__(self):
        '''
        Just a simple exception
        '''
        super().__init__()
