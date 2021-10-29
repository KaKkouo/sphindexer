import os, sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Sphindexer Testcase'
copyright = '2021, @KoKekkoh'
author = 'Kakkouo, KoKekkoh'

release = '0.2.0'

extensions = ['src']
templates_path = ['_templates']
language = 'ja'
exclude_patterns = []

#kana_text_separator = r'\|'
#kana_text_option_marker = r'\^'
#kana_text_indexer_mode = 'small'
#kana_text_word_file = '~/sphinx/word_list.txt'
#kana_text_on_genindex = True
#kana_text_change_triple = True
