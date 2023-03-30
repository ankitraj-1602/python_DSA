class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val,end=" ")
        inorder_traversal(root.right)
def preorder_traversal(root):
    if root:
        print(root.val,end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val,end=" ")
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
insert(root.left,444)
inorder_traversal(root)
