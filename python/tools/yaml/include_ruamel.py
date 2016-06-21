"""
Litterally copy/pasted from
https://gist.github.com/joshbode/569627ced3076931b02f
I don't know if the author put a licence, but he said
he would probably use MIT.
I only changed the parameters of __init__
to make it compatible with pyaml and ruamel.yaml
"""

from ruamel import yaml
import os.path

class LoaderMeta(type):

    def __new__(metacls, __name__, __bases__, __dict__):
        """Add include constructer to class."""

        # register the include constructor on the class
        cls = super().__new__(metacls, __name__, __bases__, __dict__)
        cls.add_constructor('!include', cls.construct_include)

        return cls


class Loader(yaml.Loader, metaclass=LoaderMeta):
    """YAML Loader with `!include` constructor."""

    def __init__(self, stream, version):
        """Initialise Loader."""

        try:
            self._root = os.path.split(stream.name)[0]
        except AttributeError:
            self._root = os.path.curdir

        super().__init__(stream)

    def construct_include(self, node):
        """Include file referenced at node."""

        filename = os.path.abspath(os.path.join(
            self._root, self.construct_scalar(node)
        ))
        extension = os.path.splitext(filename)[1].lstrip('.')

        with open(filename, 'r') as f:
            if extension in ('yaml', 'yml'):
                return yaml.load(f, Loader)
            else:
                return ''.join(f.readlines())
