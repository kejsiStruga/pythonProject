class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self.post_order_traversal(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False

    def pre_order_traversal(self, subtree, traversal_str):
        """Root -> Left -> Right"""
        if subtree:
            traversal_str += (str(subtree.value) + "-")
            traversal_str = self.pre_order_traversal(subtree.left, traversal_str)
            traversal_str = self.pre_order_traversal(subtree.right, traversal_str)
        return traversal_str

    def in_order_traversal(self, subtree, traversal_str):
        """Left -> Root -> Right"""
        if subtree:
            traversal_str = self.in_order_traversal(subtree.left, traversal_str)
            traversal_str += (str(subtree.value) + "-")
            traversal_str = self.in_order_traversal(subtree.right, traversal_str)
        return traversal_str

    def post_order_traversal(self, subtree, traversal_str):
        """Left->Right->Root"""
        if subtree:
            traversal_str = self.post_order_traversal(subtree.left, traversal_str)
            traversal_str = self.post_order_traversal(subtree.right, traversal_str)
            traversal_str += (str(subtree.value) + "-")
        return traversal_str


if __name__ == '__main__':
    #            1
    #         /     \
    #        2       3
    #       / \     / \
    #      4   5   6   7
    #                   \
    #                    8

    binary_tree = BinaryTree(1)
    # creating a left child of the root node
    binary_tree.root.left = Node(2)
    # creating a right child of the root node
    binary_tree.root.right = Node(3)
    binary_tree.root.left.left = Node(4)
    binary_tree.root.left.right = Node(5)
    binary_tree.root.right.left = Node(6)
    binary_tree.root.right.right = Node(7)
    binary_tree.root.right.right.right = Node(8)
    print("PreOrder Traversal: " + binary_tree.print_tree("preorder"))
    print("InOder Traversal: " + binary_tree.print_tree("inorder"))
    print("PostOder Traversal: " + binary_tree.print_tree("postorder"))
