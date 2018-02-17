import numpy as np

def main():
    print(matrix_tutorial())

def matrix_tutorial():
    A = np.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])

    # 1
    tmp=np.mean(A)*12
    B=A/(tmp)
    # 
    #print(np.var(B))
    return np.var(B)

if __name__ == "__main__":
    main()
