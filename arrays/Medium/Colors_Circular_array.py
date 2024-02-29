def shortest_color_segment(input_arr):

    if len(input_arr) == 0 or len(input_arr) < 3:
        return -1
    
    start_index = 0
    shortest_segment = float('inf')

    input_extended = input_arr * 2

    left , right = 0, 0

    n = len(input_arr)

    color_dict = {}

    while right < len(input_extended):
        # O(2n)

        color = input_extended[right]
        if color in color_dict:
            color_dict[color] += 1
        else:
            color_dict[color] = 1
        
        while len(color_dict) == 3 and left <= right: 
            if right - left + 1 < shortest_segment:
                shortest_segment = right - left + 1
                start_index = left % n
        
            color_dict[input_extended[left]] -= 1
            if color_dict[input_extended[left]] == 0:
                del color_dict[input_extended[left]]
            left += 1
        
        right += 1
    

    return (start_index, shortest_segment)


input1 = ['r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'g']
input1 = []
input1 = ['r', 'r', 'r', 'b', 'b', 'b', 'b', 'b']

res = shortest_color_segment(input1)

print(res)



        


