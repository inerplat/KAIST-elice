import numpy

def matrix_tutorial():
    A = numpy.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])

    # 1
    B = A.reshape((6,2))
    # 2
    T = numpy.array([[2,2],[5,3]])
    B = numpy.concatenate((B,T),axis = 0)
    # 3
    tmp = numpy.split(B,2,axis=0)
    C=tmp[0]
    D=tmp[1]
    # 4
    E = numpy.concatenate((C,D),axis=1)
    # 5
    return E

print(matrix_tutorial())
