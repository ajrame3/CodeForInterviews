class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        [1, 2, 3, 6] k = 9
        k = 3
        [1, 2]
        [3]
        left, right = 0
        sstart a loop (left, len(nums))


        count += 1

        [1, 2, 3, -3], k = 3
        # I did not conside negative
        sum(L, R) = sum(R) - sum(L-1)
        Sum(R) = 3 R = 4
        k = sum(R) - sum(L-1)
        sum(L-1) = sum(R) - k
        
        left = 0
        right = 0
        cur_win_total = nums[0]
        count = 0

        while left < len(nums):
            if left > right:
                right = left
                cur_win_total = nums[left]
            
            if cur_win_total < k:
                right += 1
                if right == len(nums):
                    break
                cur_win_total += nums[right]
            elif cur_win_total > k:
                cur_win_total -= nums[left]
                left += 1
            else:
                count += 1
                cur_win_total -= nums[left]
                left += 1
        
        return count
        '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        dict = {}
        counter = 0

        for i in range(len(nums)):
            total += nums[i]
            if total == k:
                counter += 1

            if (total - k) in dict:
                counter += dict[total - k]
            
            if total in dict:
                dict[total] += 1
            else:
                dict[total] = 1
        return counter