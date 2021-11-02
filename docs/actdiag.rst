ACTION DIAGRAM
==============

.. actdiag::

  write ->  get -> domain -> entries
  -> entry -> make -> unit -> units
  -> update -> sort -> generate
  -> index -> handle

  lane builder {
    label = "builder"
    write [label = "write_index()"]
    handle [label = "handle_page()"]
  }

  lane IndexRack {
    get [label = "env.get_domain()"]
    entry
    update [label = "update_units()"]
    sort [label = "sort_units()"]
    index [label = "return: genindex"]
  }

  lane IndexUnit {
    unit
  }

  lane IndexEntry {
    make [label = "make_index_units"]
    units [label = "return: unts"]
  }

  lane Environment {
    domain [label = "domain.entries"]
    entries [label = "retrun: entries"]
  }
