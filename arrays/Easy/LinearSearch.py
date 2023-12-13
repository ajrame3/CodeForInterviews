def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    
    if n == 0:
        return -1
    
    for i in range(n):
        if arr[i] == num:
            return i
    
    return -1