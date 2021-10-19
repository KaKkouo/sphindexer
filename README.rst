A sphinx extension to replace the IndexEntries class.

- Sphindexer = Sphinx + Indexer

THE GOAL
--------
- It's to become the IndexEntries class.
- It has the extention for kana_text.

FEATURE
-------

- Even when editing glossary with index_key, make clean is not necessary.
- See/seealso appears at the end.
- When there are multiple functions with the same name, the first one will not be left out.
- It is relatively easy to customize the display order to your liking.

    - You must be able to develop sphinx extensions.

USAGE
-----

conf.py

.. code-block:: python

   extensions = ['sphindexer']

build ( without sphindexer ):

.. code-block:: sh

   $ make html 

build ( with sphindexer ):

.. code-block:: sh

   $ make idxr
