class Globals:

    __stack = None
    __player = None
    
    @staticmethod
    def init(key, val):
        if key == 'stack':
            Globals.__stack = val
            return
        if key == 'player':
            Globals.__player = val
            return
        raise NameError(f"can't set {key} value")

    @staticmethod
    def stack():
        return Globals.__stack

    @staticmethod
    def pipe():
        return Globals.__stack.top

    @staticmethod
    def player():
        return Globals.__player

    pass


