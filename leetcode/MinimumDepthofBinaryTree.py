# -*- coding:utf-8 -*-
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        if root is None:
            return 0
        tmplist1 = [root]
        tmplist2 = []
        count = 1
        while True:
            for node in tmplist1:
                if self.leaf(node):
                    #print('1')
                    return count   
                elif node.left is not None and node.right is not None:
                    tmplist2.append(node.left)
                    tmplist2.append(node.right)
                elif node.right is not None:
                    tmplist2.append(node.right)
                else:
                    tmplist2.append(node.left)
            tmplist1, tmplist2 = tmplist2, tmplist1
            tmplist2 = []
            count += 1
                
    def leaf(self, node):
        if node.left is None and node.right is None:
            return True
        return False
