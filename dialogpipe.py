'''
A specific pipe to be used to simplify text dialogs
'''

from pipe import Pipe
from directions import Direction
from structures import PipeText
from pipelements import PipeElement, Interactable
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
        super().__init__(pipe, asp, (0,-1))

    def move(self, direct: 'Direction') -> bool:
        if direct == Direction.Up:
            if self._xy[0] == 0:
                return False
            self._xy = (self._xy[0]-1, self._xy[1])
            return True
        elif direct==Direction.Down:
            if self._xy[0] == len(self._pipe._rows) -1:
                return False
            self._xy = (self._xy[0] + 1, self._xy[1])
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
            PipeElement.__init__(self, pipe, self._normal, (i, 0))
            if text:
                PipeText(pipe, (i, 1), text)
                pass
        else:
            PipeElement._init__(self, pipe, self._normal, (index, 0))
            if text:
                PipeText(pipe, (index, 1), text)
                pass
            pass
        pass

    def hover(self, val: bool):
        self._aspect = {True: self._hover, False: self._normal}[val]
        return
    
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

class DialogPipe(Pipe):
    '''
    DialogPipe class.
    '''
    def __init__(self, dialog_txt: str, *args):
        Pipe.__init__(self)
        PipeText(self, (0, 0), dialog_txt)
        self._avatar = Cursor(self)
        
        #TODO: add options to pipe
        
        pass

    def print(self, term_sizes, **kwargs):
        '''
        Prints the pipe content inside the rect 'term_sizes',
        showing dialog text + options
        '''
        print(aspects.FRAME*term_sizes[1])
        if max(self._rows) > term_sizes[0] and self.avatar.row > term_size[0]:
            for r in range(self._avatar.row - term_size[0], term_size[0]):
                self.get_row(r).print(term_sizes[1], -2)
                pass
            pass
        else:
            for r in range(term_sizes[0]):
                self.get_row(r).print(term_sizes[1], -2)
                pass
            pass
        print(aspects.FRAME*term_sizes[1])
        
        return
    
    pass

