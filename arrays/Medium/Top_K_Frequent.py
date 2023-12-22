class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return -1
        
        res = []
        count_dict = defaultdict(int)
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        for num in sorted(count_dict, key=count_dict.get, reverse=True):
            if k == 0:
                return res
            else:
                res.append(num)
                k -= 1
        
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return -1
        
        res = []
        lookup = [[] for i in range(len(nums)+1)]
        count_dict = defaultdict(int)
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        for key, value in count_dict.items():
            lookup[value] = key
        
        for i in range(len(lookup)-1, -1, -1):
            for n in lookup[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res


