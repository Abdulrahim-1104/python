class Node:
    def __init__(self,value):
        self.key = value
        self.right = None
        self.left = None
        self.height = 0
class AVL:
    # initalizing constructor
    def __init__(self,root):
        self.root = Node(root)

    # calculating the heightt
    def get_height(self,node):
        if node is None:
            return -1
        return node.height
    def left_rotate(self,z):
        # inializing
        y = z.right
        t2 = y.left
        # linking
        y.left = z
        z.right = t2

        # modifying heigt after rotation
        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height= 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y
    def right_rotate(self,z):
        # initializing
        y = z.left
        t3 = y.right
        # linking
        y.right = z
        z.left = t3
        # updating height afer linking
        z.height = 1 + max(self.get_height(z.left),self.get_height(z.right))
        y.height= 1 + max(self.get_height(y.left),self.get_height(y.right))
        return y

    # traversal
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key,' and its height is ',root.height)
        self.inorder(root.right)

    # insert
    def insert_key(self,value):
        self.root = self.insert(self.root,value)

    def insert(self,root,value):
        if root is None:
            return Node(value)
        elif root.key > value:
            root.left = self.insert(root.left,value)
        elif root.key < value:
            root.right = self.insert(root.right,value)
        else:
            root  return

        # after inserting updating the height to the ansertor
        root.height = 1 + max(self.get_height(root.left),self.get_height(root.right))
        balanced_factor = self.get_height(root.left) - self.get_height(root.right)

        # LL case
        if balanced_factor > 1 and value < root.left.key:
            return self.right_rotate(root)
        # LR case
        if balanced_factor > 1 and value > root.left.key:
           root.left = self.left_rotate(root.left)
           return self.right_rotate(root)
        # RR case
        if balanced_factor < -1 and value > root.right.key:
            return self.left_rotate(root)
        # RL case
        if balanced_factor < -1 and value < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

avltree = AVL(50)
avltree.insert_key(20)
avltree.insert_key(60)
avltree.insert_key(10)
avltree.insert_key(30)
avltree.insert_key(40)

avltree.inorder(avltree.root)

# deleting the node is same as binary tree