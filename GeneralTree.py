class TreeNode:
    def __init__(self, func=None):
        self.val = func
        self.children = []

    def set_value(self, new_func):
        self.val = new_func

    def delete_value(self):
        self.val = None

    def add_child(self, child=None):
        if not child:
            child = TreeNode()
        self.children.append(child)


class GeneralTree:
    def __init__(self, root: TreeNode = None):
        if not root:
            root = TreeNode()
        self.root = root

    def execute(self, num):
        return rec_execute(self.root, num)


def rec_execute(root, num):
    if not root:
        return 'no root'

    result = root.val(num)
    for child in root.children:
        result = rec_execute(child, result)
    return result


def func1(x):
    return x * x


def func2(x):
    return x // 10


def func3(x):
    return 1 - x


def func4(x):
    return abs(x)


tree_root = TreeNode(func1)

child1 = TreeNode(func2)
child2 = TreeNode(func3)
child3 = TreeNode(func4)

tree_root.add_child(child1)
tree_root.add_child(child2)
tree_root.children[1].add_child(child3)      # child2.add_child(child3)

gtree = GeneralTree(tree_root)

print(gtree.execute(13))   # -> 15
