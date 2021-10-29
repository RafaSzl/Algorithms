"""
Implement a binary tree using Python, and show its usage with some examples
"""


# Here's a simple class representing a node within a binary tree.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Let's create objects representing each node of the above tree
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

# We can connect the nodes by setting the .left and .right properties of the root node.
node0.left = node1
node0.right = node2

# We can create a new variable tree which simply points to the root node,
# and use it to access all the nodes within the tree
tree = node0

# It's a bit inconvenient to create a tree by manually connecting all the nodes.
# Let's write a helper function which can convert a tuple with the structure
# ( left_subtree, key, right_subtree) (where left_subtree and right_subtree are themselves tuples) into binary tree.
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(tree_tuple)

print(tree2.key)
print(tree2.left.key, tree2.right.key)
print(tree2.left.left.key)
print(tree2.left.right)
print(tree2.right.left.right.key)
print(tree2.right.right.right.key)
# A function doing opposite of parse_tuple:


def display_keys(node, space='\t', level=0):
    # print (node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return

    # If node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


display_keys(tree2, ' ')



