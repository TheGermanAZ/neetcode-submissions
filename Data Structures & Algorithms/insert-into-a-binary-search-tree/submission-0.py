class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = TreeNode(val)
        curr = root
        while curr:
            if curr.val < val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = node
                    break
            else:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    break
        return root