"""
Data Reader file. This file is to include the functionality to
read in the data from the NETTalk data files retrieved from the
following link: https://archive.ics.uci.edu/ml/machine-learning-databases/
                undocumented/connectionist-bench/nettalk/nettalk.data
Team: Belinda Adam, Jacquelyn Haughey
Machine Learning 2015 Final Project
Phonological Learning of English Pronunciation
"""

import re

def readDataFile(datafile):
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
    words = []
    prons = []

    i = 0
    # read each line from the file
    for line in f:
        line.strip()
        example = line.split()

        # the length of the line will be four only with examples
        # gunpowder is missing the syllable structure, so it only has 3
        if len(example) == 3 or len(example) == 4:
            word = example[0]
            pron = example[1]

            # add the example to the lists
            i += 1
            ex = (word, pron)
            examples.append(ex)
            words.append(word)
            prons.append(pron)

    # close file
    f.close()

    # return the lists
    return examples, words, prons
