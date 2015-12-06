"""
Tester file: This file will run all of the important parts of the project.
Team: Belinda Adam, Jacquelyn Haughey
Machine Learning 2015 Final Project
Phonological Learning of English Pronunciation
"""

import DataReader as dataReader
import Network

# read data from the nettalk data set
f = 'nettalk.data.txt'
examples, words, prons = dataReader.readDataFile(f)
numExamples = len(examples)
print 'The list has ' + str(numExamples) + ' examples!'

# how to get first 5 examples in the data set using the tuples
i = 0
for example in examples:
    if i < 5:
        i += 1
        print example[0] + ' is pronounced like ' + example[1]



network = Network.Network([examples[0]], 0, 27, 40, 51, 0.3)
network.train_network()
