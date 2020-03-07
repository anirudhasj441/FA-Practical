class Node:
    
    def __init__(self,index):
        
        self.left=None
        self.right=None
        self.val=index
        
def insert(root,newnode):
    if root is None:
        root=newnode
    else:
        if root.val<newnode.val:
            if root.right is None:
                root.right=newnode
            else:
                insert(root.right,newnode)
        else:
            if root.left is None:
                root.left=newnode
            else:
                insert(root.left,newnode)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(100)
insert(r,Node(20))
insert(r,Node(10))
insert(r,Node(50))
insert(r,Node(120))
insert(r,Node(102))
insert(r,Node(180))
print("Inorder traversal of a tree is:")
inorder(r)
        
