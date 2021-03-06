from src import IndexRack

class domain(object):
    def __init__(self, entries):
        self.entries = entries

class env(object):
    def __init__(self, entries):
        self.domain = {}
        self.domain['index'] = domain(entries)
    def get_domain(self, domain_type):
        return self.domain[domain_type]

class config(object):
    def __init__(self):
        self.kana_text_separator = r'\|'
        self.kana_text_indexer_mode = 'normal'
        self.kana_text_word_file = ''
        self.kana_text_word_list = ()
        self.html_kana_text_on_genindex = False
        self.html_change_triple = False

class builder(object):
    def __init__(self, env):
        self.env = env
        self.get_domain = env.get_domain
        self.config = config()
    def get_relative_uri(self, uri_type, file_name):
        return f'{file_name}.html'

class IndexEntries(IndexRack):
    def __init__(self, env):
        self.env = env
        self._kana_catalog = {}
        super().__init__(builder(env))
    def create_index(self, builder, group_entries = True):
        self.builder = builder
        self.config = builder.config
        self.get_relative_uri = builder.get_relative_uri
        return super().create_index(group_entries)
