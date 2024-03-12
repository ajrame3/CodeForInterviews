# 670 MAximum Swap

class Solution:
    def maximumSwap(self, num: int) -> int:

        if num <= 11:
            return num
        
        num_arr = collections.deque([])

        while num:
            num_arr.appendleft(num % 10)
            num //= 10
        
        max_seen = -1
        max_seen_at = len(num_arr)

        i = len(num_arr) - 1

        while i >= 0:
            cur_num = num_arr[i]
            num_arr[i] = (cur_num, max_seen, max_seen_at)
            if cur_num > max_seen:
                max_seen = cur_num
                max_seen_at = i
            
            i -= 1
        
        i = 0 
        while i < len(num_arr):
            cur_num, max_to_right, max_seen_at = num_arr[i]
            if max_to_right > cur_num:
                num_arr[i], num_arr[max_seen_at] = num_arr[max_seen_at], num_arr[i]
                break
            
            i += 1
        
        num = 0
        for cur_num, _, _ in num_arr:
            num = num * 10 +cur_num
        
        return num