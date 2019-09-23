"""
The approach here is do a bfs traversal and at every level keep the first element as the max element and
in that particular level traversal check if greater elements exisits. if so update max and finally append
max to the output array.
Time complexity - O(N)
space complexity - O(N)
Leetcode running.
"""
def largestValues(self, root):
        if not root:
            return []
        
        result = []
        level = [root]
        
        while level:
            new_level = []
            max_val = float('-inf')
            
            for node in level:
                if node.val > max_val:
                    max_val = node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            result.append(max_val)
            level = new_level
        return result