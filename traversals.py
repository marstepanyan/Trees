class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root is None:
        return

    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


def preorder_traversal(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()
        print(current.data, end=" ")

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def postorder_traversal(root):
    if root is None:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        current = stack1.pop()
        stack2.append(current)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)

    while stack2:
        current = stack2.pop()
        print(current.data, end=" ")


# Creating a sample binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order Traversal:")
inorder_traversal(root)
print("\n")

print("Pre-order Traversal:")
preorder_traversal(root)
print("\n")

print("Post-order Traversal:")
postorder_traversal(root)
print("\n")
