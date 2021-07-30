class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def lca(root, v1, v2):
    if root == None:
        return root
    if root.val == v1 or root.val == v2:
        return root
    left = lca(root.left, v1, v2)
    right = lca(root.right, v1, v2)

    if left != None and right != None:
        return root
    else:
        if left != None:
            return left
        elif right != None:
            return right


root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)

ancestor = lca(root, 1, 7)
print(ancestor.val)
