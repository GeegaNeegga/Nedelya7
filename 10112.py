class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    def check(node):
        if not node:
            return 0  # Высота пустого дерева = 0

        left = check(node.left)
        if left == -1:
            return -1  # Несбалансировано

        right = check(node.right)
        if right == -1:
            return -1  # Несбалансировано

        if abs(left - right) > 1:
            return -1  # Разница высот > 1 — не сбалансировано

        return max(left, right) + 1  # Возвращаем высоту текущего поддерева

    return check(root) != -1

# Пример использования:
if __name__ == "__main__":
    # Сбалансированное дерево:
    #       1
    #      / \
    #     2   3
    #    /
    #   4

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print(is_balanced(root))  # Вывод: True

    # Несбалансированное дерево:
    #       1
    #      /
    #     2
    #    /
    #   3

    root2 = Node(1)
    root2.left = Node(2)
    root2.left.left = Node(3)

    print(is_balanced(root2))  # Вывод: False
