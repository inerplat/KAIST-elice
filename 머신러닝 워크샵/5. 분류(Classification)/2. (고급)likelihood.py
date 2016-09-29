import re
import math
training_sentence = ""
testing_sentence = ""
def main():
    # 1
    training_sentence = input()
    training_model = create_BOW(training_sentence)

    # 2
    testing_sentence = input()
    testing_model = create_BOW(testing_sentence)

    # 3
    alpha = float(input())

    print (calculate_doc_prob(training_model, testing_model, alpha))

def calculate_doc_prob(training_model, testing_model, alpha):
    # Implement likelihood function here...
    # x_i+a/N+ad
    N=sum(training_model.values())
    d=len(training_model)
    testing_sentence=list(testing_model.keys())
    training_sentence=list(training_model.keys())
    logprob=0
    boon_mo=N+d*alpha
    for i in range(0,len(testing_model)):
        x_count=testing_model[testing_sentence[i]]
        if testing_sentence[i] in training_model:
            boon_ja=training_model[testing_sentence[i]]+alpha
        else:
            boon_ja=alpha
        result=math.log(boon_ja/boon_mo)
        logprob=logprob+result*x_count
    return logprob

def create_BOW(sentence):
    bow = {} 
    sentence = sentence.lower()
    sentence = replace_non_alphabetic_chars_to_space(sentence)
    sentence = sentence.strip().split()
    for i in range(0,len(sentence)):
        if len(sentence[i]) < 1:
            del sentence[i]
    for i in range(0,len(sentence)):
        if sentence[i] in bow:
            bow[sentence[i]] = bow[sentence[i]]+1
        else:
            bow[sentence[i]] = 1
    return bow

def replace_non_alphabetic_chars_to_space(sentence):
    return re.sub(r'[^a-z]+', ' ', sentence)

if __name__ == "__main__":
    main()
