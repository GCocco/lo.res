from globals import Globals
import dialogpipe
import aspects

class Item:
    def __init__(self, name, aspect=aspects.ITEM_DEFAULT, num=1):
        self._name = name
        self._aspect = aspect
        self._num = num
        pass

    def __call__(self):
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def aspect(self):
        return self._aspect
    
    @property
    def num(self):
        return self._num

    def changeNum(self, n):
        self._num += n
        return self._num

    def toPipe(self, pipe, *args, **kwargs):
        return PipeItem(pipe, self)
    pass


class PipeItem(dialogpipe.DialogButton):
    def __init__(self, pipe, item, *args, **kwargs):
        super().__init__(pipe,
                         text=(item.name+' ' + str(item.num)),
                         normal=item.aspect,
                         command=item, *args, **kwargs)
        pass
    pass


class Inventory:
    def __init__(self):
        self._list = []
        pass


    def getItem(self, name):
        for i in range(len(self._list)):
            if self._list[i].name == name:
                return i
            pass
        return None
    
    def insert(self, item):
        i = self.getItem(item.name)
        if i != None:
            self._list[i].changeNum(num)
            return
        self._list.append(item)
        return

    def discard(self, name, num):
        if num >-1:
            raise Exception("num must be a negative number")
        i = self.getItem()
        if i == None:
            return False
        if self._list[i].num < num:
            return False
        self._list[i].changeNum(num)
        if self._list[i].num == 0:
            self._list.pop(i)
            pass
        return True

    @property
    def list(self):
        return self._list

    pass


class Player:
    def __init__(self):
        self._inventory = Inventory()
        pass

    @property
    def inventory(self):
        return self._inventory
    pass



def init():
    Globals.init('player', Player())
