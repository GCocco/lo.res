'''
A specific pipe to be used to simplify text dialogs
'''

from pipe import Pipe
from directions import Direction
from structures import PipeText
from pipelements import PipeElement
import aspects

class Cursor(PipeElement):
    '''
    A PipeElement used to navigate a DialogPipe
    '''
    def __init__(self, pipe: 'DialogPipe',
                 asp=None):
        assert isinstance(pipe, DialogPipe)
        if asp is None:
            asp = aspects.DIALOG_CURSOR
        super().__init__(pipe, asp, (0,0))

    def move(self, direct: 'Direction') -> bool:
        
        pass

class DialogPipe(Pipe):
    '''
    DialogPipe class.
    '''
    def __init__(self):
        pass
