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
        super().__init__(pipe, asp, (-1,0))

    def move(self, direct: 'Direction') -> bool:
        # TODO implement
        pass

class ButtonElement(PipeElement):
    '''
    A "button" that can be hovered by the cursor.
    It can execute a command when "hovered", when "unhovered"
    and when a button is pressed during hover'''
    def __init__(self, pipe, pos, command, *args, **kwargs):
        '''
        Base constructor.
        '''
        self._custom_normal = None
        self._custom_hover = None
        if "normal" in kwargs:
            self._custom_normal = kwargs["normal"]
        if "hover" in kwargs:
            self._custom_hover = kwargs["hover"]

        self._command = command
        self._args = args
        if self._custom_normal:
            super().__init__(pipe, self._custom_normal, pos)
        else:
            super().__init__(pipe, aspects.BUTTON, pos)
        self.update()

    def change_command(self, command, *args):
        '''
        Changes the command for this button.
        '''
        self._command = command
        if args:
            self._args = args

    def change_args(self, *args):
        '''
        Changes the args used when button is pressed
        '''
        self._args = args

    def __call__(self. *args):
        '''
        Calls the command. if arguments are given,
        they are added to the ones previously setted
        '''
        self._command(*(self._args+args))

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
            

class DialogPipe(Pipe):
    '''
    DialogPipe class.
    '''
    def __init__(self):
        self._cursor = Cursor(self) 
        pass

    def addText(self, text: str, pos=(None, None)):
        '''
        Adds a text to the pipe.
        '''
        if not pos[0]:
            rows = list(self._rows.keys())
            rows.sort()
            pos[0] = rows[len(rows)-1] + 1
        if not pos[1]:
            if pos[0] in self._rows:
                cols = self._rows[pos[0]].keys()
                pos[1] = cols[len(cols)-1] + 2
        PipeText(self, pos, text)
