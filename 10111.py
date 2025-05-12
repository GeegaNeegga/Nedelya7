class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if not root:
        return 0

    def is_leaf(node):
        return node and not node.left and not node.right

    def dfs(node):
        if not node:
            return 0
        sum_left = node.left.value if is_leaf(node.left) else 0
        return sum_left + dfs(node.left) + dfs(node.right)

    return dfs(root)

# Пример использования:
if __name__ == "__main__":
    # Пример дерева:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    #
    # Левые листья: 9 и 15

    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print(sum_of_left_leaves(root))  # Вывод: 24 (9 + 15)
