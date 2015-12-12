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

examples, words, prons = dataReader.readDataFile('random_100_train.txt')
examples2, words2, prons2 = dataReader.readDataFile('random_100_test.txt')

train = examples
test = examples2

network = Network.Network(train, test, 1, 120, 27, 53, 0.5, 1)
network.train_network()
network.test_network()
