class OccupiedSpaceError(Exception):
    def __init__(self, row_col):
        super().__init__(f"{row_col} is occupied by {Pipe.get(*row_col)}")
        pass
    pass


class Row(dict):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            pass
        elif len(args) == 1:
            super().__init__(args[0])
            pass
        elif len(args) == 2:
            super().__init__({args[0]: args[1]})
            pass
        else:
            raise Exception("Invalid arguments for Row " + args)
        pass

    def keys(self):
        l = list(super().keys())
        l.sort()
        return l

    def pop(self, key: int):
        if key in self:
            super.pop(key)
            return
        return
    pass

class Pipe:
    _rows = dict()

    @staticmethod
    def add(row, col, obj):
        if row in Pipe._rows:
            if Pipe._rows[row].get(col):
                raise OccupiedSpaceError((row, col))
            Pipe._rows[row][col] = obj
            return
        Pipe._rows[row] = Row(col, obj)
        return

    @staticmethod
    def get(row: int, col: int):
        if row in Pipe._rows:
            return Pipe._rows.get(col)
        return None

    @staticmethod
    def get_row(row: int):
        if row in Pipe._rows:
            return Pipe._rows[row]
        return Row()
    
    @staticmethod
    def delete(row: int, col: int) -> Row:
        if row in self._rows:
            Pipe._rows[row].pop(col)
            if len(Pipe._rows[row]) == 0:
                Pipe._rows.pop(row)
            return Row()
        return
    
    pass
