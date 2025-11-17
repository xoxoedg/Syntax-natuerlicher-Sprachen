import nltk

from nltk.tree import Tree
from nltk.parse.generate import generate

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> PROPN
    VP -> V NP
    PROPN -> "Maria" | "Moritz"
    V -> "sieht"
""")

sent = "Maria sieht Moritz"
parser = nltk.ChartParser(grammar)

for sentence in generate(grammar, depth=5):
    print(' '.join(sentence))
