class Globals:

    __stack = None

    
    @staticmethod
    def init(key, val):
        if key == 'stack':
            Globals.__stack = val
            return
        raise NameError(f"can't set {key} value")

    @staticmethod
    def stack():
        return Globals.__stack

    @staticmethod
    def pipe():
        return Globals.__stack.top

    pass


