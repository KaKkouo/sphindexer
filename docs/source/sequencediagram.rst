SEQUENCE DIAGRAM
================

.. seqdiag::

   Builder -> IndexRack;
   Builder -> IndexRack [label = "CALL: create_index"];
     IndexRack -> IndexEntry;
     IndexRack -> IndexEntry [label = "CALL: make_index_units"];
     IndexRack <-- IndexEntry [label = "return: units"];
     IndexRack -> IndexRack [label = "CALL: update_units"];
     IndexRack -> IndexRack [label = "CALL: sort_units"];
   Builder <-- IndexRack [label = "return: genindex"];
