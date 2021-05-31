'''
Here are defined Classes to easy handle the screen printing.
'''

class OccupiedSpaceError(Exception):
    '''
    Exception raised when attempting to place a PipeElement in an already occupied slot.
    '''
    def __init__(self, pipe: 'Pipe', row_col):
        '''
        Your basic Exception constructor
        '''
        super().__init__(f"{row_col} is occupied by {pipe.get(*row_col)}")
        self.collided = pipe.get(*row_col)


class Row(dict):
    '''
    Abstraction of a row. Only occupied slots are stored.
    '''
    def __init__(self, *args):
        '''
        Multiple constructors:
        Row()
        Row({int: PipeElement})
        Row(int, PipeElement)
        '''
        if len(args) == 0:
            super().__init__()
        elif len(args) == 1:
            super().__init__(args[0])
        elif len(args) == 2:
            super().__init__({args[0]: args[1]})
        else:
            raise Exception("Invalid arguments for Row " + args)

    def keys(self) -> 'list[int]':
        '''
        Returns the set of keys as a sorted list
        '''
        key_list = list(super().keys())
        key_list.sort()
        return key_list

    def pop(self, key: int):
        '''
        Overrides dict.pop().
        Doesn't raise KeyError if the key is not in the dictionary
        '''
        if key in self:
            return super().pop(key)
        return None


class Pipe:
    '''
    An abstraction of the screen matrix, contains the vaious rows.
    '''

    def __init__(self):
        '''
        Pipe constructor
        '''
        self._rows = dict()
        self._avatar = None

    def add(self, row: int, col: int, obj: 'PipeElement'):
        '''
        Adds a PipeElement in the row,col slot
        '''
        if row in self._rows:
            if self._rows[row].get(col):
                raise OccupiedSpaceError(self, (row, col))
            self._rows[row][col] = obj
            return
        self._rows[row] = Row(col, obj)

    def set_avatar(self, avatar: 'Avatar'):
        '''
        Sets the given avatar as the Pipe avatar.
        Used for printing format
        '''
        self._avatar = avatar

    @property
    def avatar(self) -> 'Avatar':
        '''
        Returns the avatar for this pipe, or None if it isn't defined
        '''
        return self._avatar

    def get(self, row: int, col: int) -> 'union[PipeElement, None]':
        '''
        Returns the PipeElement in the given Slot, None if empty.
        '''
        if row in self._rows:
            return self._rows.get(col)
        return None

    def get_row(self, row: int) -> 'Row':
        '''
        Returns the Row at given index
        '''
        if row in self._rows:
            return self._rows[row]
        return Row()

    def delete(self, row: int, col: int) -> 'Row':
        '''
        Deletes the PipeElement from the given Slot. If the row is emptied, it gets canceled.
        '''
        if row in self._rows:
            self._rows[row].pop(col)
            if len(self._rows[row]) == 0:
                self._rows.pop(row)
            return Row()
        return None
