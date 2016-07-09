.. role:: yaml(code)
   :language: yaml



Yaml
====

Yaml is a data format used mainly for configuration.  The structure of
the yaml files is the same as the one of the json files, but more
human-friendly. I choosed it because json is a lot less convenient for
writing, and could discourage the users to add their own content.

The best site I found for learning Yaml is
https://learnxinyminutes.com/docs/yaml/ In case it's too long for you,
I tried to make a small introduction. But I think you really should
see the link.

.. highlight:: json

In JSON, a JS object is written::

  {
    "name": "item",
    "weight": 4
  }

.. highlight:: yaml

But written is Yaml, we have::

     name: item
     weight: 4

The nested objects are understood by the parser, using the indentation::

  name: item
  weight: 6
  lvl: 3
  stats:
    str: 20
    int: 10


.. highlight:: json

While the same json object is written::

  {
     "name": "item",
     "weight": 6,
     "lvl": 3,
     "stats": {
        "str": 20,
	"int": 10
     }
  }

.. highlight:: yaml

The json arrays, in Yaml, are written::

   - 2
   - item
   - long string

And the object arrays are written::

   -
      name: item
      weight: 6
      lvl: 3
      stats:
 	 str: 20
  	 int: 10
   - "another item"

You probably noticed that ``another item`` is between quotes. In fact,
Yaml, since 1.2, supports every correct JSON object. So all the JSON
examples will work in a Yaml parser.

Yaml also has directives, which are used by adding a ``!`` before the
directive. For example, if you type::

  value: 1

The parser will understand the ``1`` as ``true`` (probably not what
you want). There is a Yaml directive, called ``int``, used to specify
the type integer::

  value: !int 1

I also added a special directive, ``!include``, which will parse an
extern file and include the result as a value. Example::

  value: 3
  included: !include path/to/file.yml

I didn't create the code used for the ``!include`` directive, I
copy/pasted a snippet from
https://gist.github.com/joshbode/569627ced3076931b02f, in which I
adapted the arguments of the class to make it compatible with PYaml
and ruamel.yaml.
