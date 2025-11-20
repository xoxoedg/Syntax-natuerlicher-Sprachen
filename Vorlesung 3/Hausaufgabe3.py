import nltk
from nltk.tree import Tree
from nltk import CFG, Production, Nonterminal
import copy

sent_1 = 'der Hund jagt den langsamen Briefträger'

grammar = nltk.CFG.fromstring("""
    S   -> NP VP
    VP  -> V NP
    NP  -> DET N
    NP  -> DET ADJ N

    DET -> "der" | "den"
    N   -> "Hund" | "Briefträger"
    ADJ -> "langsamen"
    V   -> "jagt"python3
""")

parser = nltk.ChartParser(grammar=grammar)

parser = nltk.ChartParser(grammar)
for tree in parser.parse(sent_1.split()):
    tree.pretty_print(unicodelines=True)

