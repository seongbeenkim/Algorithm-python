def insertion_sort(data_list):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data_list[j] < data_list[j-1]:
                data_list[j],data_list[j-1] = data_list[j-1],data_list[j]
            else:
                break
    return data_list

"""
def insertion_sort(data_list):
    for i in range(len(data_list)-1):
        key = data_list[i+1]
        for j in range(i+1, 0, -1):
            if key < data_list[j-1]:
                data_list[j-1], data_list[j] = data_list[j], data_list[j-1]
            else:
                break
    return data_list
"""