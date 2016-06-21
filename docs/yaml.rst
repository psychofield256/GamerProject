Yaml
====

Yaml is a data format used mainly for configuration.
The structure of the yaml files is the same as the one of the json files,
but more human-friendly. I choosed it because json is a lot less convenient
for writing, and could discourage the users to add their own content.

I still didn't found why there is no yaml syntax highlight. Please be indulgent.

.. highlight:: json

For example, a JS object is written::

  {
    "name": "item",
    "weight": 4
  }

.. highlight:: yaml

But written is Yaml, we have::

     name: item
     weight: 4

.. highlight:: yaml

The nested objects are understood by the parser by the indentation::

  name: item
  weight: 6
  lvl: 3
  stats:
    str: 20
    int: 10

While the same json object is written::

.. code:: json

  {
     "name": "item",
     "weight": 6,
     "lvl": 3,
     "stats": {
        "str": 20, "int": 10
     }
  }

The json arrays, in Yaml, are written:

.. code-block:: yaml

   - 2
   - item
   - long string

The object arrays are written:

.. code-block:: yaml

   -
      name: item
      weight: 6
      lvl: 3
      stats:
 	 str: 20
  	 int: 10
   - another item
