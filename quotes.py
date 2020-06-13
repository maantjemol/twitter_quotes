import numpy as np

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])


def generate_chain(starting_word, n_words, ):
    text = open('quotes.txt', encoding='utf8').read()
    corpus = text.split()

    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    # Choosing a starting word
    if starting_word != str:
        starting_word = np.random.choice(corpus)
        while True:
            starting_word = np.random.choice(corpus)
            not_word = np.random.choice(word_dict[starting_word])
            # Check if it's not an name:
            if starting_word.isupper() and not_word.islower():
                break

    chain = [starting_word]

    while True:
        x = np.random.choice(word_dict[chain[-1]])
        if x.isupper():
            continue

        chain.append(x)

        if len(chain) > n_words and "." in chain[-1]:
            break

    # print(' '.join(chain))
    return ' '.join(chain)