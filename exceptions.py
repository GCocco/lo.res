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

