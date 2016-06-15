from scenes.base import Scene

class LoadSaveFileMenu(Scene):
    """
    Menu of save file selection before loading the game.
    This scene uses a goto (the adress of the load file is stored in manager.cache).
    """
    def __init__(self):
        pass
