def get_input():
    return input("Enter a sentence: ")

def p_sentence(sentence):
    words = sentence.lower().split()
    return set(words)

def main():
    sentence = get_input()
    unique_words = p_sentence(sentence)
    print("Unique words:", sorted(unique_words))

if __name__ == "__main__":
    main()
