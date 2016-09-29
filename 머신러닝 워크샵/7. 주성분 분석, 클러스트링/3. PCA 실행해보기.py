import sklearn.decomposition
import numpy as np
import pandas as pd
import elice_utils

def main():
    df = input_data()

    # 2
    pca, pca_array = run_PCA(df, 1)

    # 4
    elice_utils.draw_toy_example(df, pca, pca_array)

def input_data():
    # 1
    N=int(input())
    X = []
    Y = []
    for i in range(N):
        line=input().strip().split()
        X.append(float(line[0]))
        Y.append(float(line[1]))
    df = pd.DataFrame({'x': X, 'y': Y})

    return df

def run_PCA(df, num_components):
    # 2
    pca=sklearn.decomposition.PCA(1)
    pca.fit(df)
    pca_array = pca.transform(df)
    return pca, pca_array

if __name__ == '__main__':
    main()
