def trivial_search(l: list, v: int):
    for i in range(len(l)):
        if v == l[i]:
            return i
    return False