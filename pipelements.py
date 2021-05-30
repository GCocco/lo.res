import aspects
from directions import Direction
from pipe import Pipe


class PipeElement:

    def __init__(self, emj: str, xy: 'tuple[int, int]'):
        self._emj = emj
        self._xy: 'tuple[int, int]' = xy
        pass

    def __repr__(self) -> str:
        return self._emj
    pass


class Avatar(PipeElement):
    def __init__(self, xy: 'tuple[int, int]'):
        super().__init__(aspects.Avatar, xy)
        pass

    def move(self, direc):
        move_to: 'tuple[int, int]'

        if direc == Direction.Up:
            move_to = self._xy[0] - 1, self._xy[1]
            pass
        elif direc == Direction.Right:
            move_to = self._xy[0], self._xy[1] + 1
            pass
        elif direc == Direction.Down:
            move_to = self._xy[0] + 1, self._xy[1]
            pass
        elif direc == Direction.Left:
            move_to = self._xy[0], self._xy[1] - 1
            pass
        else:
            raise Exception("argument must be a valid Direction")

        if Pipe.get(*move_to):
            return False
        Pipe.delete(*self._xy)
        Pipe.add(*move_to, self)
        self._xy = move_to
        return True

    pass
