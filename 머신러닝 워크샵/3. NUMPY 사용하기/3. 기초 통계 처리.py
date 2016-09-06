import numpy

def matrix_tutorial():
    A = numpy.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])
    B = A.reshape((6, 2))
    B = numpy.concatenate((B, numpy.array([[2, 2], [5, 3]])), axis = 0)
    (C, D) = numpy.split(B, 2, axis = 0)
    E = numpy.concatenate((C, D), axis = 1)

    # 1
    E=E/numpy.sum(E)
    # 2
    variance=numpy.var(E)
    return variance

print(matrix_tutorial())
