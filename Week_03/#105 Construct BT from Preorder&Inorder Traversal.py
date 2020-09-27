# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def reBuildTree(pre_left, pre_right, in_left, in_right):
            # 终止条件
            if pre_left > pre_right:
                return None

            # process
            # 1. 当前根节点取值(每次递归的pre_left为根节点在前序的位置)
            pre_root = pre_left

            # 2. 找到根节点在中序的位置
            in_root = index[preorder[pre_left]]

            # 3. 当前左子树的大小
            size_left_tree = in_root - in_left

            # 4. 构造根节点
            root = TreeNode(preorder[pre_root])

            root.left = reBuildTree(pre_left + 1, pre_left + size_left_tree, in_left, in_right - 1)

            root.right = reBuildTree(pre_left + 1 + size_left_tree, pre_right, in_root + 1, in_right)

            return root

        n = len(preorder)

        index = {element: i for i, element in enumerate(inorder)}
        return reBuildTree(0, n - 1, 0, n - 1)