def cy_test(int x):
    '''useless function to increment y x times'''
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i
    return y