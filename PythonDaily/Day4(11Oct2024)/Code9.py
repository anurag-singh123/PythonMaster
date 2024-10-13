# Implement functions to serialize (convert to string) and deserialize (convert back to tree) a binary tree in Python.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):

    if not root:
        return "X,"  # Use "X" to represent None

    left_serialized = serialize(root.left)
    right_serialized = serialize(root.right)

    return str(root.val) + "," + left_serialized + right_serialized

def deserialize(data):
  
    nodes = data.split(",")

    def deserialize_helper(nodes):
        val = nodes.pop(0)
        if val == "X":
            return None

        node = TreeNode(int(val))
        node.left = deserialize_helper(nodes)
        node.right = deserialize_helper(nodes)

        return node

    return deserialize_helper(nodes)

# Example usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Serialize the binary tree
serialized_tree = serialize(root)
print("Serialized tree:", serialized_tree)

# Deserialize the string back to a binary tree
deserialized_root = deserialize(serialized_tree)
print("Deserialized tree:")
print(deserialized_root.val)  # 1
print(deserialized_root.left.val)  # 2
print(deserialized_root.right.val)  # 3
print(deserialized_root.right.left.val)  # 4
print(deserialized_root.right.right.val)  # 5