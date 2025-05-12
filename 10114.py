class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None

    # Меняем местами левого и правого потомков
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# Функция для вывода дерева (обратный обход для наглядности)
def print_tree(root):
    if root is not None:
        print_tree(root.right)
        print(root.value)
        print_tree(root.left)

# Пример использования:
if __name__ == "__main__":
    # До инверсии:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    invert_tree(root)

    # После инверсии:
    #       1
    #      / \
    #     3   2
    #    /     \
    #   5       4

    print_tree(root)
