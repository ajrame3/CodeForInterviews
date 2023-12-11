def TwoSum(arr, target):
    if len(arr) == 0:
        return
    
    dict = {}

    for i in range(len(arr)):
        secNum = target - arr[i]
        if secNum in dict:
            return (dict[secNum], i)     
        else:
            dict[arr[i]] = i 