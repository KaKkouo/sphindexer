STRUCTURE
=========
structure of the data for genindex.html

.. index:: data structure; entry

- entry: {file_name: [(entry_type, value, target, main, index_key)]}

    - file_name: the name without suffix
    - entries: [entry]

        - entry: (entry_type, value, target, main, index_key)

            - entry_type: in('single', 'pair', 'triple', 'see', 'seealso')
            - value: 'word', 'word; word' or 'word; word; word'
            - target: the target id
            - main: 'main' or ''
            - index_key: classifier or None

.. index:: data structure; genindex

- genidex: [(classifier, terms)]

    - classifier: textclass
    - terms: [(term, list)]

        - term: textclass
        - list: [links, subterms, index_key]

            - links: [(main, uri)]
            - subterms: [(subterm, links)]

                - subterm: SubTerm[textclass]
                - links: [(main, uri)]

            - index_key: str

variables

- term: a textclass object.
- rawword: a term.
- rawtext: ex. 'term', 'term1; term2' or 'term1; term2; term3'
- rawsouce: means Element.rawsource.
- textclass: for extention. IndexRack -> IndexEntry -> IndexUnit.
- text: (T.B.D.)

methods

- astext: return a string like a eacy identifier

.. index:: class; IndexEntry

IndexEntry

- object['entry_type']: 'single', 'pair', 'triple', 'see' or 'seealso'
- object[0]: textclass(rawword)
- object[1]: textclass(rawword)
- object[2]: textclass(rawword)
- object['file_name']: a file name
- object['target']: a target id
- object['main']: 'main' or ''
- object['index_key']: None or classifier
- object.make_index_unit(): return [IndexUnit, IndexUnit, ...]

.. index:: class; IndexRack

IndexRack

- object[n]: IndexUnit(...)
- object.append(): update classifier_catalog and function_catalog
- object.extend(): call the object.append() by each IndexUnit object
- object.udpate_units(): update IndexUnit object with all catalog
- object.sort_units(): to be sorted
- object.generate_genindex_data()

.. index:: class; IndexUnit

IndexUnit

- object[0]: textclass(classifier)
- object[1]: textclass(main term)
- object['link']: code (1:'see', 2:'seealso', 3:'uri')
- object[2]: SubTerm([], [textclass(2nd)], or [textclass(2nd), textclass(3rd)])
- object['emphasis']: code (1:recseved, 2:reserved, 3:'main', 4:'')
- object['file_name']: target file
- object['target']: target id
- object['main']: emphasis
- object['index_key']: None or classifier
- object.get_children: return [object[1], object[2][0], object[2][1]]

.. index:: class; Subterm

Subterm

- object[0]: textclass
- object[1]: textclass
- object.delimiter: ' ' or ', '
