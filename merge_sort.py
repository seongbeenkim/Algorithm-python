def merge_sort(left,right):
    sorted_list = list()
    left_index, right_index = 0, 0
    
    while len(left) > left_index and len(right) > right_index:
        if left[left_index] > right[right_index]:
            sorted_list.append(right[right_index])
            right_index += 1
        else:
            sorted_list.append(left[left_index])
            left_index += 1
    while len(left) > left_index:
        sorted_list.append(left[left_index])
        left_index += 1
        
    while len(right) > right_index:
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list

def split(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = split(data[:medium])
    right = split(data[medium:])
    return merge_sort(left,right)