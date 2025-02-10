class Node:
    # constructor
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None
class binarysearchtree:
    # constructor
    def __init__(self,value):
        self.root = Node(value)

    # inserting values in tree
    def insert(self,root,value):
        if root == None:
            return Node(value)
        if root.key > value:
            root.left = self.insert(root.left,value)
        else:
            root.right = self.insert(root.right,value)
        return root

    def insert_value(self,value):
        self.insert(self.root,value)

    # search operation
    def search(self,root,value):
        if root == None or root.key == value:
            return root
        if root.key > value:
            return self.search(root.left,value)
        else:
            return self.search(root.right,value)

    # deleting Node
    def delete(self,root,value):
        if root.key > value:
            root.left = self.delete(root.left,value)
        elif root.key < value:
            root.right = self.delete(root.right,value)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                root.key = self.min(root.right)
                root.right = self.delete(root.right,root.key)
        return root

    def min(self,root):
        if root.left is None:
            return root.key
        return self.min(root.left)

    # preorder traversal
    def preorder(self,root):
        if root is None:
            return
        print(root.key, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
    # inorder traversal
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key,end=' ')
        self.inorder(root.right)
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.key,end=' ')

root = 50
bst = binarysearchtree(root)
bst.insert_value(20)
bst.insert_value(70)
bst.insert_value(10)
bst.insert_value(25)
bst.insert_value(60)
bst.insert_value(90)
bst.insert_value(80)
bst.insert_value(75)
print('Pre order traversal ')
bst.preorder(bst.root)
print('\n\npost order traversal')
bst.postorder(bst.root)
print('\n\nIn order traversal')
bst.inorder(bst.root)
# deleting node
bst.delete(bst.root,50)
# after deletion
print('\nAfter deletion')
bst.inorder(bst.root)
result = bst.search(bst.root,20)
if result == None:
    print('\nValue not found')
else:
    print('\nValue found')

