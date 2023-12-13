def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    if len(a) == 0:
        return -1
    
   # douche bag --> Sliding Window -adjust the window on left

    left = 0
    cur_sum = 0
    max_len = 0

    for right in range(len(a)):
        cur_sum += a[right]

        while cur_sum > k and left <= right:
            cur_sum -= a[left]
            left += 1
        
        if cur_sum == k:
            max_len = max(max_len, right - left + 1)
    
    return max_len if max_len > 0 else -1
        