from enum import IntEnum

class PipeElement:

    def __init__(self, emj: str):
        self._emj = emj
        pass

    def __repr__(self) -> str:
        return self._emj
    pass
