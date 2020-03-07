class Node:
    def __init__(self,index):
        self.index=index
        self.left=None
        self.right=None
def Inorder(root):
    if root is not None:
        Inorder(root.left)
        print(root.index),
        Inorder(root.right)
def Preorder(root):
    if root is not None:
        print(root.index)
        Preorder(root.left),
        Preorder(root.right)
def Inorder(root):
    if root is not None:
        Inorder(root.left)
        Inorder(root.right),
        print(root.index)
def insert(node,index):
    if node is None:
        return Node(index)
    if index<node.index:
        node.left=insert(node.left,index)
    else:
        node.right=insert(node.right,index)
    return root

root=insert(root,100)
root=insert(root,20)
root=insert(root,10)
root=insert(root,80)
root=insert(root,120)
root=insert(root,102)
root=insert(root,180)
print("Inorder traversal of a tree is:")
Inorder(root)
print("Preorder traversal of a tree is:")
Preorder(root)
print("Postorder traversal of a tree is:")
Postorder(root)






















        
        
