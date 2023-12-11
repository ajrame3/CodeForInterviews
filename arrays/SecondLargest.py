def getSecondOrderElements(n: int,  a: [int]) -> [int]:

    if n == 0 or n == 1:
        return -1
    
    smallest = int(1e9)
    second_smallest = int(1e9)
    largest = int(-1e9)
    second_largest = int(-1e9)
    
    for i in range(n):
        smallest = min(smallest, a[i])
        largest = max(largest, a[i])
    
    for i in range(n):
        if a[i] < second_smallest and a[i] != smallest:
            second_smallest = a[i]
        if a[i] > second_largest and a[i] != largest:
            second_largest = a[i]

    return [second_largest, second_smallest]