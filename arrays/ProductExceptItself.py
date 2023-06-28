# https://leetcode.com/problems/product-of-array-except-self/

def ProductArray(arr):
    results = []
    length = len(arr)

    left_running_product  = [1] * length
    right_running_product = [1] * length

    for i in range(1, length):
        left_running_product = left_running_product[i - 1] * input[i - 1]
        end_indx = length - 1 - i
        right_running_product[end_indx] = right_running_product[end_indx + 1] * input[end_indx + 1]
    
    for i in range(length):
        left_product = left_running_product[i]
        right_product = right_running_product[i]
        product_except_self = left_product * right_product
        results.append(product_except_self)

    return results