from sklearn.neural_network import MLPClassifier
import numpy as np
import elice_utils

def main():
    # 1
    X, Y = read_data('case_0.txt') # try to use different datasets

    clf = train_MLP_classifier(X, Y)
    report_clf_stats(clf, X, Y)
    elice_utils.visualize(clf, X, Y)

def train_MLP_classifier(X, Y):
    # 2
    clf = MLPClassifier(hidden_layer_sizes=(5)) # try changing the number of hidden layers

    clf.fit(X, Y)

    return clf

def report_clf_stats(clf, X, Y):
    # 1. measure accuracy
    hit = 0
    miss = 0

    for x, y in zip(X, Y):
        if clf.predict([x])[0] == y:
            hit += 1
        else:
            miss += 1

    print("Accuracy: %.1lf%%" % float(100 * hit / (hit + miss)))

def read_data(filename):
    X = []
    Y = []

    with open(filename) as fp:
        N, M = fp.readline().split()
        N = int(N)
        M = int(M)

        for i in range(N):
            line = fp.readline().split()
            for j in range(M):
                X.append([i, j])
                Y.append(int(line[j]))

    X = np.array(X)
    Y = np.array(Y)
    return (X, Y)

if __name__ == "__main__":
    main()
