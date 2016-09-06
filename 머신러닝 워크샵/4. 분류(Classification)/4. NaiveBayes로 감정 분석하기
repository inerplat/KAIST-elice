import io
import numpy
import naivebayes_utils
import re
import math
import os

def main():
    # Implement main function for Emotion Classifier
    training1_sentences = read_text_data('./txt_sentoken/pos/')
    training2_sentences = read_text_data('./txt_sentoken/neg/')
    testing_sentence = input()

    alpha = 0.1
    prob1 = 0.5
    prob2 = 0.5

    prob_pair = naive_bayes(training1_sentences, training2_sentences, testing_sentence, alpha, prob1, prob2)

    plot_title = testing_sentence
    if len(plot_title) > 50: plot_title = plot_title[:50] + "..."
    visualize_boxplot(plot_title,
                  list(prob_pair),
                  ['Positive', 'Negative'])


def naive_bayes(training1_sentence, training2_sentence, testing_sentence, alpha, prob1, prob2):
    # Exercise
    bow_train1 = create_BOW(training1_sentence)
    bow_train2 = create_BOW(training2_sentence)
    bow_test = create_BOW(testing_sentence)

    classify1 = math.log(prob1) + log_likelihood(bow_train1, bow_test, alpha)
    classify2 = math.log(prob2)+ log_likelihood(bow_train2, bow_test, alpha)
    return normalize_log_prob(classify1, classify2)

def read_text_data(directory):
    # We already implemented this function for you
    files = os.listdir(directory)
    files = [f for f in files if f.endswith('.txt')]

    all_text = ''
    for f in files:
        all_text += ' '.join(open(directory + f).readlines()) + ' '

    return all_text

def log_likelihood(training_model, testing_model, alpha):
    return naivebayes_utils.calculate_doc_prob(training_model, testing_model, alpha)

def normalize_log_prob(prob1, prob2):
    return naivebayes_utils.normalize_log_prob(prob1, prob2)

def calculate_doc_prob(training_model, testing_model, alpha):
    return naivebayes_utils.calculate_doc_prob(training_model, testing_model, alpha)

def create_BOW(sentence):
    return naivebayes_utils.create_BOW(sentence)

def visualize_boxplot(title, values, labels):
    naivebayes_utils.visualize_boxplot(title, values, labels)

if __name__ == "__main__":
    main()
