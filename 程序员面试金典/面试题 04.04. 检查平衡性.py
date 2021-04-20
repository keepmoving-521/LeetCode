"""
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：
任意一个节点，其两棵子树的高度差不超过 1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
返回 false 。
"""


#  方法一（自顶向下的递归）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)


#  方法二：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def height(root):
            if not root:
                return 0
            leftheight = height(root.left)
            rightheight = height(root.right)
            if leftheight == -1 or rightheight == -1 or abs(leftheight - rightheight) > 1:
                return -1
            else:
                return max(leftheight, rightheight) + 1

        return height(root) >= 0


"""
方法一：自顶向下的递归
定义函数height，用于计算二叉树中的任意一个节点 p 的高度：
有了计算节点高度的函数，即可判断二叉树是否平衡。
具体做法类似于二叉树的前序遍历，即对于当前遍历到的节点，首先计算左右子树的高度，
如果左右子树的高度差是否不超过 1，再分别递归地遍历左右子节点，
并判断左子树和右子树是否平衡。这是一个自顶向下的递归的过程。
复杂度分析
时间复杂度：O(n ^ 2)，其中 n 是二叉树中的节点个数。
最坏情况下，二叉树是满二叉树，需要遍历二叉树中的所有节点，时间复杂度是 O(n)。
空间复杂度：O(n)，其中 n 是二叉树中的节点个数。空间复杂度主要取决于递归调用的层数，
递归调用的层数不会超过 n。

方法二：自底向上的递归
方法一由于是自顶向下递归，因此对于同一个节点，函数 height 会被重复调用，导致时间复杂度较高。
如果使用自底向上的做法，则对于每个节点，函数height 只会被调用一次。

自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，
再判断以当前节点为根的子树是否平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），
否则返回 -1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。
复杂度分析
时间复杂度：O(n)，其中 n 是二叉树中的节点个数。
使用自底向上的递归，每个节点的计算高度和判断是否平衡都只需要处理一次，
最坏情况下需要遍历二叉树中的所有节点，因此时间复杂度是 O(n)。

空间复杂度：O(n)，其中 n 是二叉树中的节点个数。空间复杂度主要取决于递归调用的层数，
递归调用的层数不会超过 n。
"""
