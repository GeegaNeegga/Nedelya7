class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree(root):
    if not root:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

# Пример использования:
if __name__ == "__main__":
    # Пример дерева:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(sum_tree(root))  # Вывод: 15 (1+2+3+4+5)
