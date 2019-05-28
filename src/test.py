# Passing by reference and passing by value

def mult2(n):
    return n * 2

# return list mutated
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
    return l

# returns a new list
def mult2_list_comp(l):
    return [i * 2 for i in l]
