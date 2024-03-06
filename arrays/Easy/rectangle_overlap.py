# 836

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        [blx1, bly1, trx1, try1], [blx2, bly2, trx2, try2] = rec1, rec2
        if bly2 >= try1 or blx2 >= trx1 or bly1 >= try2 or blx1 >= trx2:
            return False
        elif blx1 == trx1 or bly1 == try1 or bly2 == try2 or blx2 == trx2:
            return False
        
        return True
        