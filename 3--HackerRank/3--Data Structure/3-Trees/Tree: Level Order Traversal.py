

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def levelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        GivelevelOrder(root, i)

def GivelevelOrder(root, level):
    if root is None:
        return

    if level == 1:
        print(root.info, end=' ')

    elif level > 1:
        GivelevelOrder(root.left, level-1)
        GivelevelOrder(root.right, level-1)
def height(root):
    if root is None:
        return 0
    return max(1 + height(root.left), 1 + height(root.right))
