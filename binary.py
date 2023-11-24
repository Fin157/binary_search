def binary_search(l: list | tuple, v: int):
    start_index = 0
    end_index = len(l) - 1
    
    if start_index > end_index:
        return
    
    while start_index <= end_index:
        index = (start_index + end_index) // 2
        if v > l[index]:
            start_index = index + 1
        elif v < l[index]:
            end_index = index - 1
        else:
            return index
    return False