'''
Module containing predefined PipeElements structures.
'''
from pipelements import from_string

class PipeElementStruct:
    '''
    Main class handling multiple PipeElemnts combined into one structure.
    '''
    def __init__(self, pipe: 'pipe.Pipe', xy: 'tuple[int, int]',
                 element_list: 'list[str]'):
        '''
        Base constructor.
        Elements of the structure is given as a matrix ([[]]) of PipeElements as tuple.
        Blank spaces in the matrix are defined as None.
        Elements are placed right-down of the given position.
        '''
        self._elements: 'list[PipeElement]' = []
        self._pipe = pipe
        row_offset, col_offset = 0, 0
        for row in element_list:
            for element in row:
                if element is not None:
                    self._elements.append(from_string(element)(pipe,
                                                               (xy[0] + row_offset,
                                                                xy[1]+col_offset)))
                col_offset += 1
            col_offset = 0
            row_offset += 1

    def delete(self):
        '''
        Deletes the entire structure from the pipe
        '''
        for element in self._elements:
            element.delete()

    def add(self):
        '''
        Adds the element of the structure to the pipe
        '''
        for element in self._elements:
            element.add(self._pipe, element.xy)

    @property
    def elements(self):
        '''
        Returns the structure's PipeElements
        '''
        return self._elements


class PipeTreeBox(PipeElementStruct):
    '''
    A test structure defining a box of trees opened at the top
    '''
    def __init__(self, pipe, pos):
        '''
        Base Constructor.
        '''
        super().__init__(pipe, pos, [['Tree', 'Tree', None, 'Tree', 'Tree'],
                                     ['Tree', None, None, None, 'Tree'],
                                     ['Tree', None, None, None, 'Tree'],
                                     ['Tree', None, None, None, 'Tree'],
                                     ['Tree', 'Tree', 'Tree', 'Tree', 'Tree']])


class PipeText(PipeElementStruct):
    '''
    A String that can be easily added to the pipe as such.
    '''
    def __init__(self, pipe, pos, text: str):
        '''
        Base constructor, takes the standards PipeElement arguments + the string
        '''
        charlist = [text[i: i+2] for i in range(0, len(text), 2)]
        if len(charlist[len(charlist)-1]) == 1:
            charlist[len(charlist)-1] += ' '
        super().__init__(pipe, pos, [charlist])
