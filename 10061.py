def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root  # указатель на минимальный узел
