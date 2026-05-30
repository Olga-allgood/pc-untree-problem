# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def convert(tree):
# Your solution here!
    
    d = {}
    def traverse(node):
        if node:
            if not node.left and not node.right:
                d[node.value] = (None, None)

            elif not node.left:
                d[node.value] = (None, node.right.value)
            elif not node.right:
                d[node.value] = (node.left.value, None) 
            else:      
                d[node.value] = (node.left.value, node.right.value)  

            traverse(node.left)
            traverse(node.right)
    traverse(tree)    
    return  d   








    




r"""
       d
      / \
     e   v
"""
tree = Node("d", Node("e"), Node("v"))
print(convert(tree))

r"""
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
"""
tree = Node("a", Node("x", Node("e"), Node("m")), Node("y", None, Node("p")))
assert convert(tree) == {
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}

r"""
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z
"""
tree = Node("g", Node("e", Node("k", Node("w"))), Node("f", None, Node("d", None, Node("z"))))
assert convert(tree) == {
    "g": ("e", "f"),
    "e": ("k", None),
    "k": ("w", None),
    "w": (None, None),
    "f": (None, "d"),
    "d": (None, "z"),
    "z": (None, None),
}

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
