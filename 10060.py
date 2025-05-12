class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(root):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)            # Левое поддерево
        dfs(node.right)           # Правое поддерево
        result.append(node.value) # Корень

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

    print(postorder_traversal(root))  # Вывод: [4, 5, 2, 3, 1]
