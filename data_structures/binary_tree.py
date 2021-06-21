from my_queue import Queue


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
        elif traversal_type == "levelorder":
            # as the level order traversal is done in an iterative fashion => we don't need
            # to pass the empty string as param
            return self.level_order_traversal(self.root)
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

    def level_order_traversal(self, start_node):
        if start_node is None:
            return

        queue_ds = Queue()
        queue_ds.enqueue(start_node)

        traversal_str = ""

        while len(queue_ds) > 0:
            traversal_str += str(queue_ds.peek()) + "-"
            # next we take this node out of the queue and check for the children of that node
            # for that we use the dequeue() function because that will return the element
            node = queue_ds.dequeue()

            if node.left:
                queue_ds.enqueue(node.left)
            if node.right:
                queue_ds.enqueue(node.right)

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
    print("LevelOrder Traversal: " + binary_tree.print_tree("levelorder"))
