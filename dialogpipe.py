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
        if direct == Direction.Up:
            if self._xy[0] == 0:
                return False
            self._xy[0]-=1
            return True
        elif direct ==Direction.Down:
            if self._xy[0] == len(self._pipe._rows9 -1):
                return False
            self._xy[0] += 1
            return True
        else:
            # TODO implement opt navigation
            return False
        return False

    '''
    When called, interacts with the option pointed
    '''
    def __call__(self):
       print(self._pipe.get(*self._xy))
       return
    pass


class DialogButton(PipeElement):
    '''
    A "button" to be attached to a text label to display an option
    '''
    def __init__(self, pipe, text=None, command=None, index=None, *args, **kwargs):
        self._normal = aspects.DIALOG_BUTTON
        self._hover = aspects.DIALOG_BUTTON_HOVERED
        if command:
            self._command = command
            pass

        self._args = args
        
        if "normal" in kwargs:
            self._normal = kwargs["normal"]
            kwargs.pop("normal")
            pass
        if "hover" in kwargs:
            self._normal = kwargs["hover"]
            kwargs.pop("hover")
            pass

        self._kwargs = kwargs

        if index == None:
            i = len(pipe.rows)
            PipeElement(self, pipe, self._normal, (i, 0))
            if text:
                PipeText(pipe, (i, 1), text)
                pass
        else:
            PipeElement(self, pipe, self._normal, (index, 0))
            if text:
                PipeText(pipe, (index, 1), text)
                pass
            pass
        pass
    
    def setCommand(self, command):
        self._command = command
        return

    def setArgs(self, *args, append=False, **kwargs):
        if append:
            self._args += args
            self._kwargs.update(kwargs)
            return
        self._args = args
        self._kwargs = kwargs
        return
    
    def __call__(self):
        self._command(*args, **kwargs)
        pass
    pass


            

        
"""
TODO LATER
    
class PipeTextOption(PipeText):
    '''
    An option described by a text
    '''
    def __init__(self, pipe, pos, text: str, checked: bool=False):
        # TODO COMPLETE
        super().__init__(pipe,
                         (pos[0], pos[1] + 2),
                         text)
        self._checked = checked
            
    def toggle(self):
        '''
        Toggles the value of self._checked and updates it's aspect.
        '''
        self._checked = not self._checked
        if self._checked:
            self._opt = 

"""            

class DialogPipe(Pipe):
    '''
    DialogPipe class.
    '''
    def __init__(self, str: dialog_txt, *args):
        self._cursor = Cursor(self)
        PipeText(self, (0, 0), dialog_text)
        for opt in args:
            #TODO: add options to pipe
            pass
        pass
    
