class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    """Preorder serialization with '#' for None, space-separated."""
    vals = []

    def dfs(node):
        if node is None:
            vals.append("#")
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return " ".join(vals)


def deserialize(s):
    """Rebuild tree from preorder tokens."""
    if not s:
        return None

    tokens = iter(s.split())

    def dfs():
        val = next(tokens)
        if val == "#":
            return None
        node = Node(val)  # Keep as string
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()
