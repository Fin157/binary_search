def binary_search(l: list | tuple, v: int):
    # Initialize working area indices
    start_index = 0
    end_index = len(l) - 1
    
    # Make sure the list contains at least one element
    if start_index > end_index:
        return
    
    # Shrink the working area until it is of length 1 and less
    while start_index <= end_index:
        index = (start_index + end_index) // 2
        if v > l[index]:
            # The item is in the upper half of the working area
            start_index = index + 1
        elif v < l[index]:
            # The item is in the lower half of the working area
            end_index = index - 1
        else:
            # We've found the item at the current index
            return index
        
    # The seeked item is not present in the list
    return False