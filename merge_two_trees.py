# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_merge_trees:
    def print_tree(self,node):
        if node is None:
            return
        print(str(node.val)+"-")
        self.print_tree(node.left)
        self.print_tree(node.right)
        return
    
    def two_tree_traversal(self,t1_node,t2_node,node):
        if (t1_node is None) and (t2_node is None): 
            return None
        elif (t1_node is None):
            left_arg = (None,t2_node.left)
            right_arg = (None,t2_node.right)
            node = TreeNode(t2_node.val)
        elif (t2_node is None): 
            left_arg = (t1_node.left,None)
            right_arg = (t1_node.right,None)
            node = TreeNode(t1_node.val)
        else: 
            left_arg = (t1_node.left,t2_node.left)
            right_arg = (t1_node.right,t2_node.right)
            node = TreeNode(t1_node.val+t2_node.val)
        #print("current node value",node.val)
        node.left = self.two_tree_traversal(left_arg[0],left_arg[1],node.left)
        node.right = self.two_tree_traversal(right_arg[0],right_arg[1],node.right)
        return node
    
    def mergeTrees(self, t1, t2):
        root_node = TreeNode()
        root_node = self.two_tree_traversal(t1,t2,root_node)
        #self.print_tree(root_node)
        return root_node
