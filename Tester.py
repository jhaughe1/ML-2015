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

middle = int(len(examples)/10000)
# train = examples[0:middle]
train = [examples[2]]
# test = examples[middle:2*middle]
test = train

network = Network.Network(train, test, 1, 27, 20, 53, 0.5, 1000)
network.train_network()
network.test_network()
#print network.hiddenW
