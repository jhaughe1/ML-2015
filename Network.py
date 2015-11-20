"""
Network file. This file will run a neural network to the specifications
described in the project writeup.
Team: Belinda Adam, Jacquelyn Haughey
Machine Learning 2015 Final Project
Phonological Learning of English Pronunciation
"""

import numpy as np

class Node:
    def __init__(self, index, type_node):
        # set activation
        self.activation = 0.0
        if type_node == "input":
            self.symbol = getLetterForIndex(index)
        elif type_node == "output":
            # add output symbol?
            self.symbol = getPhonForIndex(index)

    def setActivation(new_activation):
        self.activation = new_activation

    def getActivation(self):
        return self.activation

    def getSymbol(self):
        return self.symbol

def runNetwork(examples, num_neighbors, num_input, num_hidden, num_output):

    ### NETWORK SETUP ###
    input_units = []
    for x in range(num_input):
        node = Node(x, "input")
        input_units.append(node)

    hidden_units = []
    for x in range(num_hidden):
        node = Node(x, "hidden")
        hidden_units.append(node)

    output_units = []
    for x in range(num_output):
        node = Node(x, "output")
        output_units.append(node)

    weights_IH = np.zeros([num_input, num_hidden])
    weights_HO = np.zeros([num_hidden, num_output])

    for i in range(num_input):
        row = weights_IH[i]
        for j in range(num_hidden):
            weights_IH[i, j] = np.random.uniform(-0.3, 0.3)

    for i in range(num_hidden):
        row = weights_HO[i]
        for j in range(num_output):
            weights_HO[i, j] = np.random.uniform(-0.3, 0.3)

    ### TRAIN NETWORK ###
    #for t in range(len(examples)):
    #    target = examples[t]
    # print input_units[0].getSymbol()

def getIndexForLetter(letter):
    return (ord(letter) - ord('a'))

def getLetterForIndex(index):
    return chr(index + ord('a'))

def getPhonForIndex(index):
    return 'X'
