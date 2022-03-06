Inspect to hgdb
---------------

Proof-of-concept symbol table conversion from LegUp symbol table
(Inspect) to hgdb.

Currently supported feature:

- breakpoints
- context signals

Not yet supported:

- RAM information. Inspect create a main memory controller that's
  hardcoded into the system. Getting values out from this
  memory controller unit requires some engineering work.


Usage
=====
Once installed, simply do

.. code-block::

    inspect2hgdb [output.db]

This will read out local MySQL connection and dump the hgdb
symbol to ``output.db``.

Install
=======

Simply do

.. code-block::

  pip install .

