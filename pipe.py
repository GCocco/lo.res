'''
Here are defined Classes to easy handle the screen printing.
'''

from exceptions import OccupiedSpaceError
from json import load, dump
from pipelements import from_string
from aspects import BLANK, FRAME

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

    def print(self, term_col: int, from_col: int):
        '''
        Prints the content of the row, starting from 'from_col' in a terminal of 'term_col' columns
        '''
        print(FRAME, end='')
        k = from_col + 2
        for lmnt_col in self.keys():
            if lmnt_col <= from_col + 1:
                continue
            if lmnt_col >= from_col+term_col:
                break
            print(BLANK*(lmnt_col-k) + self[lmnt_col].aspect, end='')
            k = lmnt_col + 1
        print(BLANK*((from_col+term_col)-k) + FRAME)

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

    def print(self, term_sizes, from_row=0, from_col=0):
        '''
        Prints the pipe content inside the rect 'term_sizes',
        placed in the from_row, crom_col slot.
        '''
        print(FRAME*term_sizes[1])
        for row_index in range(from_row, from_row + term_sizes[0]):
            self.get_row(row_index).print(term_sizes[1], from_col)
        print(FRAME*term_sizes[1])

    def add(self, obj: 'PipeElement'):
        '''
        Adds a PipeElement in the row,col slot
        '''
        if obj.row in self._rows:
            if self._rows[obj.row].get(obj.col):
                raise OccupiedSpaceError(self, obj.row, obj.col)
            self._rows[obj.row][obj.col] = obj
            return
        self._rows[obj.row] = Row(obj.col, obj)

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
            return self._rows[row].get(col)
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

    @staticmethod
    def fromlist(pipe_list):
        '''
        constructs and returns a pipe with given list of PipeElements given as list
        '''
        new_pipe = Pipe()
        for lmnt in pipe_list:
            from_string(lmnt[0])(new_pipe, lmnt[1])
        return new_pipe

    def as_list(self):
        '''
        Returns the pipe as a list of pipelements as tuples
        '''
        pipe_list = []
        for row in self._rows:
            for col in self._rows[row]:
                pipe_list.append(self._rows[row][col].as_tuple())
        return pipe_list

    def dump(self, filename: str):
        '''
        Saves the pipe as a json file.
        If the given file already exists, is overwritten.
        '''
        file_pointer = open(filename, "w")
        dump(self.as_list(), file_pointer)
        file_pointer.close()

    @staticmethod
    def load(filename) -> 'Pipe':
        '''
        Loads a saved pipe from given file.
        '''
        file_pointer = open(filename, "r")
        new_pipe = Pipe.fromlist(load(file_pointer))
        file_pointer.close()
        return new_pipe
