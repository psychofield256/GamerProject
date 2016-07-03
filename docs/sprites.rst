.. _sprites:

=======
Sprites
=======

Everything have a sprite. And if you want to add something to the game, then the thing you add needs a sprite. If you are not a graphist, but want to train, I'd be pleased that you do while creating your contents for my game.

As I'm not a graphist myself, I had to use resources from opengameart.

The file must be an image. The size is arbitrary (the image will be resized before printing). The files must be placed in: ``resources/<items|skills|monsters>/<id>.png``

For monsters, the sprite is an animation. Thus, the file will be a spritesheet, containing frames organized as follow:


+-------------+-------------+-----+
| Direction 1 | Direction 2 | ... |
+=============+=============+=====+
| South 1     | South 2     | ... |
+-------------+-------------+-----+
| North 1     | North 2     | ... |
+-------------+-------------+-----+
| East 1      | East 2      | ... |
+-------------+-------------+-----+
| West 1      | West 2      | ... |
+-------------+-------------+-----+


.. highlight:: yaml	

Monster must have the following attributes
For monsters, ``sprite`` must be set to::
  sprite:
    frames: 2
    height: 16
    width: 16
    id: blablabla
    extension: .png

The path will set to: resources/monsters/blablabla.png

For items, the ``sprite`` attribute must be filled with::

  path: relative/or/absolute/path/to/file.png


