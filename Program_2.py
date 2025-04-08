# Time Complexity = O(n)
# Space Complexity = O(n)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.helper(root)!=-1


    
    def helper(self,root):
        if root == None:
            return 0 
        

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left == -1 or right == -1:
            return -1 

        if abs(left-right)>1:
            return -1 

        return max(left,right)+1
