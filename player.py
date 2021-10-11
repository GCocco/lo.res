class _Item:
    def __init__(self, name, aspect, num=1):
        self._name = name
        self._aspect = aspect
        self._num = num
        pass

    @property
    def name(self):
        return self._name
    
    @property
    def num(self):
        return self._num

    def changeNum(self, n):
        self._num += n
        return self._num
    
    pass

class Inventory:
    def __init__(self):
        self._list = None
        pass


    def getItem(self, name):
        for i in range(len(self._list)):
            if self._list[i].name == name:
                return i
            pass
        return None
    
    def insert(self, name, aspect, num=1):
        if num <1:
            raise Exception("num must be >0")
        i = self.getItem(name)
        if i != None:
            self._list[i].changeNum(num)
            return
        self._list.append(_Item(name, aspect, num=num))
        # TODO: Items may differ and should be inheritable
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

    
    
    pass

