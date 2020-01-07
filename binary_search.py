def binary_search(data_list,search):
    print(data_list)
    if len(data_list)<=1:
        if data_list[0] == search:
            return True
        else:
            return False
        
    medium = len(data_list) // 2
    
    if data_list[medium] == search:
        return True
    elif data_list[medium] > search:
        return binary_search(data_list[:medium],search)
    else:
        return binary_search(data_list[medium+1:],search)