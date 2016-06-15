from collections import deque

from scenes.menus.main import MainMenu

class SceneManager(object):
    """Class of the scene manager."""

    def __init__(self):
        "Create the title scene"
        self.scene_stack = deque()
        self.add(MainMenu())
        self.ended = False
        self.cache = {} # used for scenes which need to store persistent data before goto-ing or go_back-ing

    def render_old(self, screen, n):
        "Render the n oldest scenes in the stack (starting from the before last one)."
        to_render = list(reversed(self.scene_stack))[1:n]
        for scene in to_render:
            scene.render(screen)

    def add(self, scene):
        self.scene_stack.append(scene)
        self.scene = scene
        scene.manager = self

    def go_back(self, n=1):
        "Remove n scene(s) from the stack"
        for _ in range(n):
            last = self.scene_stack.pop()
            last.onleave()
        if len(self.scene_stack):
            self.refresh_scene()
        else:
            self.quit()

    def go_to(self, scene):
        "Set the new scene and give (used to go to another scene without creating a sub-scene)"
        self.go_back()
        self.add(scene)
        self.scene = scene
        self.scene.manager = self

    def refresh_scene(self):
        "Synchronize the scene stack and the current scene"
        self.scene = next(reversed(self.scene_stack))

    def quit(self):
        "Brutal end. Every scene in the stack are ignored. Should only be used by MainMenu."
        self.ended = True
