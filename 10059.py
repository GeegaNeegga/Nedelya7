class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)            # Левое поддерево
        result.append(node.value) # Корень
        dfs(node.right)           # Правое поддерево

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

    print(inorder_traversal(root))  # Вывод: [4, 2, 5, 1, 3]
