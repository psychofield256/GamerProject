from ruamel import yaml
import pygame as pg

from easydict import EasyDict as edict

from constants import CONFIG_FILE, COLORS
from scenes.base import Scene
from scenes.tools.confirm import ConfirmPrompt

class SettingsMenu(Scene):
    def __init__(self):
        self.read_config_file(CONFIG_FILE)

    def read_config_file(self, filename):
        "Config is stored as json"
        with open(filename) as f:
            self.config = yaml.safe_load(f)
        self.config = edict(self.config)

    def render(self, screen):
        screen.fill(COLORS["black"])
        self.write_mid(screen, "Not implemented")
    def update(self, delta):
        pass
    def handle_events(self, events):
        for e in events:
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    self.manager.add(ConfirmPrompt("Are you sure ? Any change will be saved"))

    def onleave(self):
        pass
