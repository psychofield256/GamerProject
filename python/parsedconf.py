import os

from easydict import EasyDict as edict

from constants import *
from pprint import PrettyPrinter
import pprint

if YAML_PARSING_LIB == "ruamel.yaml":
    from ruamel import yaml
    from tools.yaml.include_ruamel import Loader
elif YAML_PARSING_LIB == "pyaml":
    import yaml
    from tools.yaml.include_pyaml import Loader

with open("config/all.yml") as f:
    conf = yaml.load(f, Loader)

p = PrettyPrinter()
p.pprint(conf)

conf = edict(conf)

for section in ('monsters', 'npcs'):
    pass

# for section in conf.entities:
#    for entity in section():
#        file = str(entity.id) = str(entity.sprite.extension)
#        entity.sprite.path = os.path.join('resources/entities', file)
