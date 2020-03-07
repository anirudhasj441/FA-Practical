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
        Inorder(root.left),
        Inorder(root.right)
def Postorder(root):
    if root is not None:
        Postorder(root.left)
        Postorder(root.right),
        print(root.index)
def insert(node,index):
    if node is None:
        return Node(index)
    if index < node.index:
        node.left=insert(node.left,index)
    else:
        node.right=insert(node.right,index)
    return node
def Searchminnode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def deleteNode(root,index):
    if root is None:
        return root
    if index <root.index:
        root.left=deleteNode(root.left,index)
    elif(index > root.index):
        root.right=deleteNode(root.right,index)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=Searchminnode(root.right)
        root.index=temp.index
        root.right=deleteNode(root.right,temp.index)
    return root
root=None
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
