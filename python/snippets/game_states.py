class State(object):
    """docstring for State"""

    def __init__(self, name, before=None):
        self.name = str(name)
        self.before = before

    def end(self):
        if self.before is not None:
            self = self.before
            return False  # False is the game is not ended
        else:
            return True

    def __str__(self):
        s = self.name
        b = self.before
        while b is not None:
            s += "->" + b.name
            b = b.before
        return s

state = State("menu")

state = State("game", state)

state = State("")

print(state)
