class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.value)  # Сначала корень
        dfs(node.left)             # Затем левое поддерево
        dfs(node.right)            # Затем правое поддерево

    dfs(root)
    return result

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

    print(preorder_traversal(root))  # Вывод: [1, 2, 4, 5, 3]
