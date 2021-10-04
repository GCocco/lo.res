class Globals:

    __vars = {'stack': None}
    
    @staticmethod
    def init(key, val):
        if key == 'stack':
            Globals.__vars['stack'] = val
            return
        raise NameError(f"can't set {key} value")

    @staticmethod
    def stack():
        return Globals.__vars['stack']

    pass


