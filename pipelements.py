'''
This module contains pipe-renderable classes.
'''
from exceptions import OccupiedSpaceError
from directions import Direction
import aspects

class PipeElement:
    '''
    Basic renderable class.
    '''

    def __init__(self, pipe: 'Pipe', emj: str, xy: 'tuple[int, int]', append=True):
        '''
        Constructor for PipeElement.
        the element is represented with emj glyph and is immediatly placed in xy.
        '''
        self._emj: str = emj
        self._xy: 'tuple[int, int]' = xy
        self._pipe = pipe
        if append:
            self._pipe.add(self)
            pass
        pass
    
    def as_tuple(self) -> str:
        '''
        Returns the Pipelement as a json-compatibile tuple
        '''
        return (self._emj, self._xy)

    def update(self):
        '''
        Removes and adds again the element to the pipe.
        Used to update the pipe since adding the element in the init superclass may cause troubles
        '''
        self.delete()
        self._pipe.add(self)

    @property
    def aspect(self) -> str:
        '''
        Returns the emoji representing this element.
        '''
        return self._emj

    @property
    def row(self) -> int:
        '''
        Returns the Row the element is placed.
        '''
        return self._xy[0]

    @property
    def col(self) -> int:
        '''
        Returns the column the element is placed.
        '''
        return self._xy[1]

    def delete(self):
        '''Deletes this element from the render pipe.'''
        return self._pipe.delete(*self._xy)


class Tree(PipeElement):
    '''
    A tree. just a PipeElement with predefined aspect.
    '''
    def __init__(self, pipe, xy):
        '''
        Basic constructor.
        '''
        super().__init__(pipe, aspects.TREE, xy)


class Interactable(PipeElement):
    '''
    An Interactable PipeElement.
    Interaction is launched by the avatar stepping on it's slot
    '''
    def __init__(self, pipe: 'Pipe',
                 lmnt_aspect: str,
                 pos: 'tuple[int, int]',
                 function=None, args=None):
        '''
        base Constructor.
        '''
        super().__init__(pipe, lmnt_aspect, pos)
        self._interact_func = function
        if self._interact_func is None:
            self._interact_func = self._voidfunc
        self._arguments = args
        self.update()

    def set_function(self, interact_func, args=None):
        '''
        Sets the given function as the function called when interaction is launched
        '''
        self._interact_func = interact_func
        self._arguments = args

    def set_args(self, args):
        '''
        Sets the given arguments to be used when interaction is called.
        '''
        self._arguments = args

    @property
    def args(self):
        '''
        Returns the arguments setted for this instance.
        '''
        return self._arguments

    def __call__(self):
        '''
        Interface used when interacting with this element
        '''
        if self._arguments:
            return self._interact_func(*self._arguments)
        return self._interact_func()

    @staticmethod
    def _voidfunc(*args):
        '''
        Blank default func.
        '''
        return args

class Avatar(PipeElement):
    '''
    PipeElement representing the avatar.
    Easier to move around and has default aspect.
    '''
    def __init__(self, pipe: 'Pipe', xy: 'tuple[int, int]'):
        '''
        Avatar constructor.
        '''
        super().__init__(pipe, aspects.AVATAR, xy)
        pipe.set_avatar(self)
        pass

    def __call__(self):
        return

    def move(self, direc: 'Direction') -> bool:
        '''
        Attempts to move the avatar of 1 unit in the given direction.
        Returns True if movement is possible, False otherwise
        '''
        move_to: 'tuple[int, int]'

        if direc == Direction.Up:
            move_to = self._xy[0] - 1, self._xy[1]
        elif direc == Direction.Right:
            move_to = self._xy[0], self._xy[1] + 1
        elif direc == Direction.Down:
            move_to = self._xy[0] + 1, self._xy[1]
        elif direc == Direction.Left:
            move_to = self._xy[0], self._xy[1] - 1
        else:
            raise Exception("argument must be a valid Direction")

        backup_pos = self._xy
        try:
            self._xy = move_to
            self._pipe.add(self)
            self._pipe.delete(*backup_pos)
            return True
        except OccupiedSpaceError as occupied:
            lmnt = occupied.lmnt
            if isinstance(lmnt, Interactable):
                lmnt()
            self._xy = backup_pos
            return False

    def as_tuple(self):
        '''
        Returns the element as a json-compatible tuple
        '''
        return ('Avatar', self._xy)

def from_string(name: str):
    '''
    Returns a PipeElement Constructor based on the given string
    '''
    return {
        'Avatar': Avatar,
        'Tree': Tree,
        }.get(name, lambda pipe, coord: PipeElement(pipe, name, coord))
