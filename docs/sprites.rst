.. _sprites:

=======
Sprites
=======

Everything have a sprite. And if you want to add something to the
game, then the thing you add needs a sprite. If you are not a
graphist, but want to train, I'd be pleased that you do while creating
your contents for my game.

As I'm not a graphist myself, I had to use resources from opengameart.

The file must be an image. The size is arbitrary (the image will be
resized before printing). The files must be placed in:
``resources/<items|skills|monsters>/<id>.png``

.. For monsters, an animation and a fight sprite are needed. I planned to do both, and 
.. For now, there is no support. I think I will do a second file for the fight sprite.
.. Thus, the file will contain the both, which will be separated before use in the code.

.. , a
.. monster resource is divided in 2 files:

.. - fs (fight sprite)
.. - mf (map frames)

.. The animation file will be a spritesheet, containing frames organized
.. as follow:

.. +-------------+-------------+-----+
..  | Direction 1 | Direction 2 | ... |
.. +=============+=============+=====+
..  | South 1     | South 2     | ... |
.. +-------------+-------------+-----+
..  | North 1     | North 2     | ... |
.. +-------------+-------------+-----+
..  | East 1      | East 2      | ... |
.. +-------------+-------------+-----+
..  | West 1      | West 2      | ... |
.. +-------------+-------------+-----+


.. highlight:: yaml	

monsters must have the following attributes::

  id: blablabla
  extension: .png

The path will become: ``resources/entities/monsters/blablabla.png``

..  sprite:
    frames: 2
    height: 16
    width: 16
    extension: .png

.. The file paths will become:

.. - resources/monsters/blablabla-fs.png
.. - resources/monsters/blablabla-mf.png

.. The path will set to: resources/monsters/blablabla.png

For items, as there is a single image, the size doesn't need to be
precised, and the ``sprite`` attribute doesn't need to be
set. Instead, the id attribute must be set::

  id: item-test
  extension: .png

Then, the path will become ``resources/items/item-test.png``

For now, the extension can't be choosen, because I still didn't found where to put an 'extension' attribute.
