#O(N) time & space
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def postorder(node):       
            if node is None:
                return "."
            left = postorder(node.left)
            right = postorder(node.right)
            hashcode = f"{left},{right},{node.val}" #fstring only supported by Python3
            print(hashcode)
            if counter[hashcode] == 1:
                duplicates.append(node)
            counter[hashcode] += 1
            return hashcode
            
        counter, duplicates = defaultdict(int), []
        postorder(root)
        return duplicates
