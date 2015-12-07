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

middle = int(len(examples)/10000)
# train = examples[0:middle]
train = examples[0:5]
# test = examples[middle:2*middle]
test = train

network = Network.Network(train, test, 1, 20, 25, 53, 1.0, 500)
network.train_network()
network.test_network()
