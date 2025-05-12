class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_leaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return root.value

    return sum_of_leaves(root.left) + sum_of_leaves(root.right)

# Пример использования:
if __name__ == "__main__":
    # Пример дерева:
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6
    #
    # Листья: 4, 5, 6 → сумма: 15

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    print(sum_of_leaves(root))  # Вывод: 15
