from globals import Globals
from windowhandler import WH


class Node:
    def __init__(self, elm, nex=None):
        self._elm = elm
        self._next = nex
        pass

    @property
    def content(self):
        return self._elm

    @property
    def next(self):
        return self._next

    pass
    

class PipeStack:
    def __init__(self):
        self._nodes = None
        pass

    @property
    def top(self):
        return self._nodes.content

    def push(self, new_pipe):
        if self._nodes:
            self._nodes = Node(new_pipe, nex=self._nodes)
            WH.update()
            return
        self._nodes = Node(new_pipe)
        WH.update()
        return

    def pop(self):
        if self._nodes == None:
            return exit()
        content = self._nodes.content
        self._nodes = self._nodes.next
        return content
    pass

def init():
    Globals.init('stack', PipeStack())
    return
