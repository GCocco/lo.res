import dialogpipe, pipe
import pipelements, structures
from globals import Globals
import player

class MainMenu(dialogpipe.DialogPipe):
    def __init__(self):
        super().__init__("Main Menu")
        self._button_start = dialogpipe.DialogButton(self, "Start Game", command=WorldMap().stack_push)

        self._button_exit = dialogpipe.DialogButton(self, "Exit", command=self.stack_pop)
        pass
    pass



class InGameMenuPipe(dialogpipe.DialogPipe):
    def __init__(self):
        super().__init__("Pause")
        dialogpipe.DialogButton(self, "Save")  # TODO: add saving
        dialogpipe.DialogButton(self, "Load")  # TODO: add load
        dialogpipe.DialogButton(self, "Inventory", lambda: InventoryPipe(push=True))
        # etc
        dialogpipe.DialogButton(self, "Back", self.stack_pop)
        dialogpipe.DialogButton(self, "Quit", exit)
        pass
    pass


class WorldMap(pipe.MapPipe):
    def __init__(self):
        super().__init__()
        structures.PipeTreeBox(self, (3,3))
        pipelements.Chest(self, (-1, -1), content=player.Item("Sasso", num=2))
        self._avatar = pipelements.Avatar(self, (0,0))
        self._keymap ={"m": InGameMenuPipe().stack_push}
        pass
    pass

class InventoryPipe(dialogpipe.DialogPipe):
    def __init__(self, push=False):
        super().__init__('Inventario')
        inv = Globals.player().inventory
        for item in inv.list:
            item.toPipe(self)
            pass

        dialogpipe.DialogButton(self, "Back", self.stack_pop)

        if push:
            self.stack_push()
            pass
        
        pass
    pass

        
