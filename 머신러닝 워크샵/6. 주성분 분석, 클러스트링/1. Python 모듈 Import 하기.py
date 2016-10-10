# import this module as 'np'
import numpy as np
# import this module as 'pd'
import pandas as pd

def main():
    A = np.array(['a', 'b', 'c', 'd', 'e'])
    idx = np.array([1, 2, 3, 4, 5])
    s = pd.Series(A, index=idx)

    print("Success!")
    return 0

if __name__ == "__main__":
    main()
