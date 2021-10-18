DEVELOPMENT
-----------
structure of the data for genindex.html

- entry: {file_name: [(entry_type, value, target, main, index_key)]}

    - file_name: the name without suffix
    - entries: [entry]

        - entry: (entry_type, value, target, main, index_key)

            - entry_type: in('single', 'pair', 'triple', 'see', 'seealso')
            - value: 'word', 'word; word' or 'word; word; word'
            - target: the target id
            - main: 'main' or ''
            - index_key: classifier or None

- genidex: [(classifier, terms)]

    - classifier: Text
    - terms: [(term, list)]

        - term: Text
        - list: [links, subterms, index_key]

            - links: [(main, uri)]
            - subterms: [(subterm, links)]

                - subterm: SubTerm[Text]
                - links: [(main, uri)]

            - index_key: str

variables

- term: a Text object.
- rawword: a term.
- rawtext: ex. 'term', 'term1; term2' or 'term1; term2; term3'
- rawsouce: means Element.rawsource.
- text: (T.B.W.)

methods

- astext: return a string like a eacy identifier
- __eq__: return a string by astext,  to be identified easily, for unittest
- __str__: return a string by ashier, for jinja2

relations

Text(extend docutil.nodes.Text)

- object.__eq__: used by unittest and IndexRack.generate_genindex_data
- object.__str__: used by jinja2.

TextUnit(T.B.D.)

- object['entry_type']: 'single', 'pair', 'triple', 'see' or 'seealso'
- object[0]: Text(rawword)
- object[1]: Text(rawword)
- object[2]: Text(rawword)
- object['file_name']: a file name
- object['target']: a target id
- object['main']: 'main' or ''
- object['index_key']: None or classifier
- object.make_index_unit(): return [IndexUnit, IndexUnit, ...]

IndexRack

- object[n]: IndexUnit(...)
- object.append(): update classifier_catalog and function_catalog
- object.extend(): call the object.append() by each IndexUnit object
- object.udpate_units(): update IndexUnit object with all catalog
- object.sort_units(): to be sorted
- object.generate_genindex_data()

IndexUnit

- object[0]: Text(classifier)
- object[1]: Text(main term)
- object.sort_order: for emphasis which means 'main'.
- object[2]: SubTerm([], [Text(2nd)], or [Text(2nd), Text(3rd)])
- object[3]: emphasis code ('main': 3, '': 5, 'see': 8, 'seealso': 9)
- object['file_name']: target file
- object['target']: target id
- object['main']: emphasis
- object['index_key']: None or classifier
- object.get_children: return [object[1], object[2][0], object[2][1]]

SubTerm

- object[0]: Text
- object[1]: Text
- object.delimiter: ' ' or ', '
