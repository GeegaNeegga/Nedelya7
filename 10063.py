class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    if root is None:
        return False  # элемент не найден
    if root.value == target:
        return True
    elif target < root.value:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)
