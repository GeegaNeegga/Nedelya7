from collections import deque

def min_depth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])  # кортеж: (узел, текущая глубина)
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth  # найден ближайший лист
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
