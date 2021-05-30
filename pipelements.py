'''
This module contains pipe-renderable classes.
'''
import aspects
from directions import Direction
from pipe import Pipe, OccupiedSpaceError


class PipeElement:
    '''
    Basic renderable class.
    '''

    def __init__(self, emj: str, xy: 'tuple[int, int]'):
        '''
        Constructor for PipeElement.
        the element is represented with emj glyph and is immediatly placed in xy.
        '''
        self._emj: str = emj
        self._xy: 'tuple[int, int]' = xy
        Pipe.add(*xy, self)

    @property
    def aspect(self) -> str:
        '''
        Returns the emoji representing this element.
        '''
        return self._emj

    def delete(self):
        '''Deletes this element from the render pipe.'''
        return Pipe.delete(*self._xy)


class Avatar(PipeElement):
    '''
    PipeElement representing the avatar.
    Easier to move around and has default aspect.
    '''
    def __init__(self, xy: 'tuple[int, int]'):
        '''
        Avatar constructor.
        '''
        super().__init__(aspects.AVATAR, xy)

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
        try:
            Pipe.add(*move_to, self)
            self.delete()
            self._xy = move_to
            return True
        except OccupiedSpaceError:
            return False
