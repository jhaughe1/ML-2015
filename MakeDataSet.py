import random

def makeDataSetPair(datafile):
    """
    readDateFile reads the nettalk.data.txt and retrieves the following:
        - a list of tuples for the examples: [(word1, pron1), (word2, pron2), ...]
        - a list of words in the dataset: [word1, word2, ...]
        - a list of pronunciations in the dataset: [pron1, pron2, ...]
    """
    # open the data file
    f = open(datafile, 'r')

    # make an empty mapping for examples
    examples = []
    examples2 = []
    # words = []
    # prons = []

    randomlines = random.sample(xrange(12, 20000), 1000)
    randomlines2 = random.sample(xrange(12, 20000), 1000)
    i = 0
    # read each line from the file
    for line in f:
        store = line
        line.strip()
        example = line.split()

        # the length of the line will be four only with examples
        if len(example) == 3 or len(example) == 4:
            # gunpowder is missing the syllable structure, so it only has 3
            if randomlines.count(i) > 0:
                # if len(example) == 3 or len(example) == 4:
                    # word = example[0]
                    # pron = example[1]

                    # add the example to the lists
                    # ex = (word, pron)

                    examples.append(store)

                    # examples.append(ex)
                    # words.append(word)
                    # prons.append(pron)

            if randomlines2.count(i) > 0:
                # if len(example) == 3 or len(example) == 4:
                    examples2.append(store)

        i += 1

    f.close()

    f1 = open('random_1000_train.txt', 'w')
    f2 = open('random_1000_test.txt', 'w')

    for example in examples:
        f1.write(example)

    for example in examples2:
        f2.write(example)

    # close file
    f1.close()
    f2.close()

    # return the lists
    # return examples, words, prons

makeDataSetPair('nettalk.data.txt')
