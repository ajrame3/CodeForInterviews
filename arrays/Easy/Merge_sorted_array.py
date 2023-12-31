def merge(nums1, m, nums2, n):

    index = m + n - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[index] = nums1[m]
            m -= 1
        else:
            nums1[index] = nums2[n]
            n -= 1
        index -= 1
    
    if m < 0:
        nums1[:n+1] = nums2[:n+1]
        

