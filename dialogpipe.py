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

"""
TODO LATER
    
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

