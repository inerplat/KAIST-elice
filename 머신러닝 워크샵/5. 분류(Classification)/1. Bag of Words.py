import re

def main():
    sentence = input()
    BOW = create_BOW(sentence)

    print(BOW)

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
