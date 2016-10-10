import sklearn.datasets
from sklearn.neural_network import MLPClassifier
import numpy as np
import random
import elice_utils

def main():
    # 1
    digits = sklearn.datasets.load_digits()
    X = digits.data
    Y = digits.target
    images = digits.images

    # 2
    X_train, Y_train, X_test, Y_test = split_data(X, Y)

    # 3
    clf = train_MLP_classifier(X_train, Y_train)
    report_clf_stats(clf, X_test, Y_test)
    # 5
    visualize(clf, X_test, Y_test, images, right = 2, wrong = 2)

def train_MLP_classifier(X, Y):
    # 4
    clf = MLPClassifier(hidden_layer_sizes=(20, 20)) # try changing the number of hidden layers

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

    print("Accuracy: %.1lf%% (%d hit / %d miss)" % (float(100 * hit / (hit + miss)), hit, miss))

def visualize(clf, X, Y, images, right, wrong):
    counter = 0
    for x, y in zip(X, Y):
        predicted = clf.predict([x])[0]
        if predicted == y:
            right -= 1
            if right < 0:
                continue
            elice_utils.display_digits(images[1600 + counter], "Right: Real value: %d (expected %d)" % (y, predicted))
        else:
            wrong -= 1
            if wrong < 0:
                continue
            elice_utils.display_digits(images[1600 + counter], "Wrong: Real value: %d (expected %d)" % (y, predicted))

        counter += 1

def split_data(X, Y):
    X_train = X[:1600]
    Y_train = Y[:1600]

    X_test = X[1600:]
    Y_test = Y[1600:]

    return X_train, Y_train, X_test, Y_test

if __name__ == "__main__":
    main()
