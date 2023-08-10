class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if not node:
            return 0
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            return max(left_height, right_height) + 1

    def get_num_nodes(self):
        return self._get_num_nodes(self.root)

    def _get_num_nodes(self, node):
        if not node:
            return 0
        else:
            left_count = self._get_num_nodes(node.left)
            right_count = self._get_num_nodes(node.right)
            return left_count + right_count + 1

    def get_root_data(self):
        if self.root:
            return self.root.data
        return

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def get_successor(self, data):
        node = self._find_node(data, self.root)
        if node:
            return None

        successor = self._find_successor(node)
        if not successor:
            return None

        return successor.data

    def _find_node(self, data, node):
        if not node or node.data == data:
            return node

        if data < node.data:
            return self._find_node(data, node.left)
        else:
            return self._find_node(data, node.right)

    def _find_successor(self, node):
        if node.right:
            return self._find_min(node.right)

        successor = None
        current = self.root

        while current:
            if node.data < current.data:
                successor = current
                current = current.left
            elif node.data > current.data:
                current = current.right
            else:
                break

        return successor

    def _insert(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def remove(self, data):
        self.root = self._remove(data, self.root)

    def _remove(self, data, node):
        if not node:
            return None

        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._remove(successor.data, node.right)

        return node

    def _find_min(self, node):          # for inorder successor
        current = node
        while current.left:
            current = current.left
        return current

    def clear(self):
        self.root = None

    def retrieve(self, data):
        return self._retrieve(data, self.root)

    def _retrieve(self, data, node):
        if not node:
            return None

        if data == node.data:
            return node.data
        elif data < node.data:
            return self._retrieve(data, node.left)
        else:
            return self._retrieve(data, node.right)

    def contains(self, data):
        return self._contains(data, self.root)

    def _contains(self, data, node):
        if not node:
            return False

        if data == node.data:
            return True
        elif data < node.data:
            return self._contains(data, node.left)
        else:
            return self._contains(data, node.right)

    def preorder_traversal(self):
        self._preorder_traversal(self.root)
        print()

    def _preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.data, end=" ")
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        self._postorder_traversal(self.root)
        print()

    def _postorder_traversal(self, node):
        if node:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.data, end=" ")


bst = BinarySearchTree()
print(bst.is_empty())  # Output: True

bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

print(bst.is_empty())  # Output: False
print(bst.get_height())  # Output: 3
print(bst.get_num_nodes())  # Output: 7
print(bst.get_root_data())  # Output: 5

bst.preorder_traversal()  # Output: 5 3 2 4 8 7 9
bst.inorder_traversal()  # Output: 2 3 4 5 7 8 9
bst.postorder_traversal()  # Output: 2 4 3 7 9 8 5

bst.remove(3)
bst.inorder_traversal()  # Output: 2 4 5 7 8 9

bst.clear()
print(bst.is_empty())  # Output: True
