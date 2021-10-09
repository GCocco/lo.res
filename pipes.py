import dialogpipe, pipe
import pipelements, structures


class MainMenu(dialogpipe.DialogPipe):
    def __init__(self):
        super().__init__("Main Menu")
        self._button_start = dialogpipe.DialogButton(self, "Start Game", command=WorldMap().stack_push)

        self._button_exit = dialogpipe.DialogButton(self, "Exit", command=self.stack_pop)
        pass
    pass


class WorldMap(pipe.MapPipe):
    def __init__(self):
        super().__init__()
        structures.PipeTreeBox(self, (3,3))
        pipelements.Chest(self, (-1, -1))
        self._avatar = pipelements.Avatar(self, (0,0))
        self._keymap ={"m": dialogpipe.InGameMenuPipe().stack_push}
        pass
    pass

