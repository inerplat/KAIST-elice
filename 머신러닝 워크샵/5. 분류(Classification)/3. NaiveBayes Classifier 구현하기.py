import re
import math
import naivebayes_utils

def main():
    training1_sentence = input()
    training2_sentence = input()
    testing_sentence = input()

    alpha = float(input())
    prob1 = float(input())
    prob2 = float(input())

    print(naive_bayes(training1_sentence, training2_sentence, testing_sentence, alpha, prob1, prob2))

def naive_bayes(training1_sentence, training2_sentence, testing_sentence, alpha, prob1, prob2):
    # Implement Naive Bayes Algorithm here...
    bow_train1 = create_BOW(training1_sentence)
    bow_train2 = create_BOW(training2_sentence)
    bow_test = create_BOW(testing_sentence)

    classify1 = math.log(prob1) + log_likelihood(bow_train1, bow_test, alpha)
    classify2 = math.log(prob2)+ log_likelihood(bow_train2, bow_test, alpha)

    return normalize_log_prob(classify1, classify2)

def normalize_log_prob(prob1, prob2):
    return naivebayes_utils.normalize_log_prob(prob1, prob2)

def log_likelihood(training_model, testing_model, alpha):
    return naivebayes_utils.calculate_doc_prob(training_model, testing_model, alpha)

def create_BOW(sentence):
    return naivebayes_utils.create_BOW(sentence)

if __name__ == "__main__":
    main()
