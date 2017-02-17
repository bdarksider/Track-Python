def distance(first, second):
    if len(first) == len(second):
        return sum([1 for  i,j in zip(first,second) if i != j])
    raise ValueError
