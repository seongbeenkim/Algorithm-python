def bubble_sort(data):
    for i in range(len(data)-1):
        swap = False
        for j in range(len(data)-1 - i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                swap = True
        if swap == False:
            break
    return data