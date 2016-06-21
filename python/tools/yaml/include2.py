"""
Copy/pasted from
http://stackoverflow.com/questions/528281/how-can-i-include-an-yaml-file-inside-another,
but the author gave another version (in include.py), so i won't use it
"""


import yaml
import os.path

class Loader(yaml.Loader):

    def __init__(self, stream, version):

        self._root = os.path.split(stream.name)[0]

        super(Loader, self).__init__(stream)

    def include(self, node):

        filename = os.path.join(self._root, self.construct_scalar(node))

        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!include', Loader.include)
