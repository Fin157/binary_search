def trivial_search(l: list, v: int):
    # Repeat for every item of the list
    for i in range(len(l)):
        if v == l[i]:
            # The current item is the value we're searching for
            return i
        
    # The target value is not present in the input list
    return False