from pygtrie import CharTrie
import os


trie = CharTrie()

trie['hi'] = 'yes'
trie['bye'] = 'no'

print 'entries'
for entry in trie:
    print entry

print list(trie['h':])
