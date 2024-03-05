#253

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        rooms = 0

        if len(intervals) == 1:
            return 1
        
        if len(intervals) == 0:
            return 0
        
        start = sorted([i[0]for i in intervals])
        end = sorted([i[1]for i in intervals])
        
        res = 0
        count = 0

        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            
            res = max(res, count)
        
        return res



        