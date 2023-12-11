def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = a[0]
    for i in range(1, n):
        if prev > a[i]:
            return 0
        else:
            prev = a[i]
    
    return 1

def isSorted(n, a):
    for i in range(1, n):
        if a[i] < a[i -1]:
            return False
    
    return True