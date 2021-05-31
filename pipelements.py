'''
This module contains pipe-renderable classes.
'''
import aspects
from directions import Direction
from exceptions import OccupiedSpaceError


class PipeElement:
    '''
    Basic renderable class.
    '''

    def __init__(self, pipe: 'Pipe', emj: str, xy: 'tuple[int, int]'):
        '''
        Constructor for PipeElement.
        the element is represented with emj glyph and is immediatly placed in xy.
        '''
        self._emj: str = emj
        self._xy: 'tuple[int, int]' = xy
        self._pipe = pipe
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
        except OccupiedSpaceError:
            self._xy = backup_pos
            return False


def from_string(name: str):
    return {
        'Avatar': Avatar,
        }.get(name, lambda pipe, coord: PipeElement(pipe, name, coord))
