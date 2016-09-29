import sklearn.decomposition
import sklearn.preprocessing
import numpy as np
import pandas as pd
import elice_utils
import scipy.spatial.distance
import operator

def main():
    # 1
    champs_df = pd.read_pickle('champ_df.pd')
    print(champs_df)
    champ_pca_array = run_PCA(champs_df, 2)

    # 5
    elice_utils.plot_champions(champs_df, champ_pca_array)
    print(get_closest_champions(champs_df, champ_pca_array, "Ashe", 10))

def run_PCA(champs_df, num_components):
    # 2

    # Normalize Attributes
    scaler = sklearn.preprocessing.MinMaxScaler()
    for champs_dim in champs_df:
        champs_df[champs_dim] =scaler.fit_transform(np.array(champs_df[champs_dim]).astype('float64'))

    # 3
    # Run PC
    pca=sklearn.decomposition.PCA(num_components)
    pca.fit(champs_df)
    champ_pca_array = pca.transform(champs_df)
    
    # 4
    return champ_pca_array

def get_closest_champions(champs_df, champ_pca_array, champ_name, num_champions):
    # Get the champion index
    champ_list = champs_df.index.tolist()
    try:
        champ_idx = champ_list.index(champ_name)
    except:
        return "%s is not in the champion list" % champ_name

    # Get the euclidean distance
    # Use scipy.spatial.distance.euclidean(A, B)
    distance_from_current_champ = {}
    for i in range(0, len(champ_list)):
        distance_from_current_champ[champ_list[i]] = \
            scipy.spatial.distance.euclidean(
                champ_pca_array[champ_idx],
                champ_pca_array[i]
            )

    # Sort dictionary according to the value
    sorted_champs = sorted(distance_from_current_champ.items(), key = operator.itemgetter(1))

    # Return top 10 champs except current one
    if num_champions > len(champ_list) - 1:
        return "num_champions is too large"
    else:
        return sorted_champs[1:1+num_champions]

if __name__ == '__main__':
    main()
