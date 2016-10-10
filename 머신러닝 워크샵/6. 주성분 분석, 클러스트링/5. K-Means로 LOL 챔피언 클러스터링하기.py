import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import numpy as np
import pandas as pd
import elice_utils
import kmeans_utils

def main():
    champs_df = pd.read_pickle('champ_df.pd')
    # 1
    champ_pca_array = run_PCA(champs_df, 2)

    champ_classes = run_kmeans(champ_pca_array, 5, [0, 30, 60, 90, 120])

    # 4
    print(elice_utils.plot_champions(champs_df, champ_pca_array, champ_classes))

    # 5
    print(get_champs_by_cluster(champs_df, champ_classes, 3))

def run_kmeans(champ_pca_array, num_clusters, initial_centroid_indices):
    # Implement K-Means algorithm using sklearn.cluster.KMeans.

    
    classifier =sklearn.cluster.KMeans(num_clusters,champ_pca_array[initial_centroid_indices], n_init=1)
    classifier.fit(champ_pca_array)
    # 3
    return classifier.labels_

def run_PCA(champs_df, num_components):
    return kmeans_utils.run_PCA(champs_df, num_components)

def get_champs_by_cluster(champs_df, champ_classes, cluster_idx):
    return champs_df.index[champ_classes == cluster_idx].values

if __name__ == '__main__':
    main()
