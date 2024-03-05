# 252

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) <= 1:
            return True
        
        intervals.sort(key = lambda i : i[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] > i2[0]:
                return False
            
        
        return True


        