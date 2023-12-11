def removeDuplicates(arr,n):
    # Write your code here.
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    left = 0
    result = 0

    for right in range(1, n):
        if arr[left] != arr[right]:
            result += 1
            left = right
    
    return result + 1