RED = False
BLACK = True


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
        self.color = RED

    def print_color(self):
        if self.color == BLACK:
            return '(b)'
        return '(r)'


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(99999)              # arbitrary value
        self.root = self.NIL
        self.NIL.color = BLACK
        self.NIL.left = None
        self.NIL.right = None

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.p = x

        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.p = x

        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x
        x.p = y

    def insert(self, key):
        z = Node(key)
        z.left = self.NIL
        z.right = self.NIL

        x = self.root                   # node being compared with z
        y = self.NIL                    # y will be parent of z
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y

        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = RED

        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p.color == RED:
            if z.p == z.p.p.left:           # is z's parent a left child?
                y = z.p.p.right             # y is z's uncle

                if y.color == RED:                  # |
                    z.p.color = BLACK               # |
                    y.color = BLACK                 # |  CASE 1
                    z.p.p.color = RED               # |
                    z = z.p.p                       # |
                else:
                    if z == z.p.right:              # |
                        z = z.p                     # |  CASE 2
                        self.left_rotate(z)         # |

                    z.p.color = BLACK               # |
                    z.p.p.color = RED               # |  CASE 3
                    self.right_rotate(z.p.p)        # |
            else:
                y = z.p.p.left
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)
            if z == self.root:
                break
            self.root.color = BLACK

    def delete(self, k):
        z = self.search(k)

        if z == self.NIL:
            return "Key not found!"

        y = z
        y_orig_color = y.color

        # CASE 1
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)            # replace z by its right child

        # CASE 2
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)            # replace z by its left child

        # CASE 3
        else:
            y = self.minimum(z.right)               # y is z's successor
            y_orig_color = y.color
            x = y.right

            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color

        if y_orig_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right               # w is x's sibling

                if w.color == RED:                      # |
                    w.color = BLACK                     # |
                    x.p.color = RED                     # |  CASE 1
                    self.left_rotate(x.p)               # |
                    w = x.p.right                       # |

                if w.left.color == BLACK:               # |
                    w.color = RED                       # |  CASE 2
                    x = x.p                             # |

                else:
                    if w.right.color == BLACK:          # |
                        w.left.color = BLACK            # |
                        w.color = RED                   # |  CASE 3
                        self.right_rotate(w)            # |
                        w = x.p.right                   # |

                    w.color = x.p.color                 # |
                    x.p.color = BLACK                   # |
                    w.right.color = BLACK               # |  CASE 4
                    self.left_rotate(x.p)               # |
                    x = self.root                       # |

            else:
                w = x.p.left
                # type 1
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotate(x.p)
                    w = x.p.left
                # type 2
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.p
                else:
                    # type 3
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.p.left
                    # type 4
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.p)
                    x = self.root
            x.color = BLACK

    def transplant(self, u, v):
        if not u.p:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def search(self, k):
        x = self.root
        while x != self.NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x
