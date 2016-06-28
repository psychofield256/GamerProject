from constants import *
from pprint import PrettyPrinter
import pprint

if YAML_PARSING_LIB == "ruamel.yaml":
    from ruamel import yaml
    from tools.yaml.include_ruamel import Loader
elif YAML_PARSING_LIB == "pyaml":
    import yaml
    from tools.yaml.include_pyaml import Loader

with open("config/items/all.yml") as f:
    conf = yaml.load(f, Loader)

p = PrettyPrinter()
p.pprint(conf)
