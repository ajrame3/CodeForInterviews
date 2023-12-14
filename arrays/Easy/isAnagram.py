class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # This code is faster than using array hash
        if len(s) != len(t):
            return False
        
        map = {}

        for eachChar in s:
            if eachChar in map:
                map[eachChar] += 1
            else:
                map[eachChar] = 1
        
        for eachChar in t:
            if eachChar in map:
                map[eachChar] -= 1
            else:
                return False
        
        for key in map:
            if map[key] != 0:
                return False
        
        return True