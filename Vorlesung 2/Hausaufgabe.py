import nltk
from nltk.tree import Tree

tree = Tree.fromstring("""
(S
    (NP (DET die)(N Studierende))
    (VP 
        (V schenkt)
        (NP(PRON(ihnen))
        (NP
            (NP (DET ein) (N Buch)) 
            (PP (P von) (NP (PROPN Chomsky)))   
        )
    )
)
)
""")
tree.pretty_print(unicodelines=True)


grammar = nltk.CFG.fromstring(
    """
    S -> NP VP
    NP -> DET N | PRON
    VP -> V NP NP
    DET -> "die" | "ein"
    PRON -> "ihnen"
    N -> "Studierende" | "Buch"
    V -> "schenkte"
    """
)

# sent = "die Studierende schenkte ihnen ein Buch"
# parser = nltk.ChartParser(grammar)
# for tree in parser.parse(sent.split()):
#     tree.pretty_print(uncodelines=True)


# Aufgabe 4