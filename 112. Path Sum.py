#https://leetcode.com/problems/path-sum/description/

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def postorder(node, path=[]):
            if node:

                path.append(node.val)

                postorder(node.left, path)

            else:
                return path
        return True




if __name__ == '__main__':
    s = Solution()
    root = TreeNode()
    
    ans = s.hasPathSum()



