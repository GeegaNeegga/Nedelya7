def inorder_successor(root, target):
    found = [False]
    result = [None]

    def inorder(node):
        if not node or result[0]:
            return
        inorder(node.left)
        if found[0] and not result[0]:
            result[0] = node
            return
        if node == target:
            found[0] = True
        inorder(node.right)

    inorder(root)
    return result[0]
