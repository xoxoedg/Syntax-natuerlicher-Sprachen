import Tree
import itertools

tree = Tree.fromstring("""
(
    (
        (
            (Die_Kunst)
            (des_Ausruhens)
        )
    )
    (
        (ist)
        (
            (ein_Teil)
            (
                (
                    (der_Kunst)
                    (des_Arbeitens)
                )
            )
        )
    )
)
""")
tree.pretty_print(unicodelines=True)


sentence = "der Postbote schrieb gestern"

permutations = list(itertools.permutations(sentence.split()))
for (i, item) in enumerate(permutations):
    print(i, item)