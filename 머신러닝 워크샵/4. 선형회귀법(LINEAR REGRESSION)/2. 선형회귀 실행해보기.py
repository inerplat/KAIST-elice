import io
import numpy
import statsmodels.api
import elice_utils


def main():
    (N, X, Y) = read_data()
    results = do_simple_regression(N, X, Y)

    elice_utils.visualize(X, Y, results)

def read_data():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        line = input().strip().split(" ")
        X.append(float(line[0]))
        Y.append(float(line[1]))
    return (N, X, Y)

def do_simple_regression(N, X, Y):
    X=numpy.array(X).T
    X=statsmodels.api.add_constant(X)
    results = statsmodels.api.OLS(Y,X).fit()
    return results

if __name__ == "__main__":
    main()
