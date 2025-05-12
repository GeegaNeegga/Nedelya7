def find_max(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root  # указатель на максимальный узел
