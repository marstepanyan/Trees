class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not root:
            return TreeNode(val)

        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # LLC
        if balance > 1 and val < root.left.val:
            print('LLC')
            return self.right_rotate(root)

        # LRC
        if balance > 1 and val > root.left.val:
            print('LRC')
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RRC
        if balance < -1 and val > root.right.val:
            print('RRC')
            return self.left_rotate(root)

        # RLC
        if balance < -1 and val < root.right.val:
            print('RLC')
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # GPT
    def search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # GPT
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        # Perform rotation
        y.left = z
        z.right = t2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        # Perform rotation
        y.right = z
        z.left = t3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # GPT
    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    # GPT
    def get_max_value_node(self, root):
        if root is None or root.right is None:
            return root
        return self.get_max_value_node(root.right)

    # GPT
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.val, end=" ")
            self.in_order_traversal(root.right)

    # GPT
    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.val, end=" ")

    # GPT
    def level_order_traversal(self, root):
        if root is None:
            return

        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(*level, end=" ")

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)


# Driver program to test above function
myTree = AVLTree()
root_node = None

root_node = myTree.insert(root_node, 10)
root_node = myTree.insert(root_node, 20)
root_node = myTree.insert(root_node, 30)
root_node = myTree.insert(root_node, 40)
root_node = myTree.insert(root_node, 50)
root_node = myTree.insert(root_node, 25)

# """The constructed AVL Tree would be
#             30
#            /  \
#          20   40
#         /  \     \
#        10  25    50"""


# Preorder Traversal
print("Preorder traversal of the constructed AVL tree is")
myTree.pre_order(root_node)
