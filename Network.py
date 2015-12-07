"""
Network file. This file will run a neural network to the specifications
described in the project writeup.
Team: Belinda Adam, Jacquelyn Haughey
Machine Learning 2015 Final Project
Phonological Learning of English Pronunciation
"""

import numpy as np
import math

class Network:

    def __init__(self, training, test, num_neighbors, num_letters, num_hidden,
                 num_phones, learning_rate, iterations):

        self.num_input = num_letters
        self.num_hidden = num_hidden
        self.num_output = num_phones
        self.window_size = 2*num_neighbors + 1
        self.data = training
        self.test_data = test
        self.learning_rate = learning_rate
        self.iterations = iterations

        self.initializeUnits()

        # initialize weights between each input segment and the hidden layer
        self.hiddenW = np.zeros([self.window_size*self.num_input, self.num_hidden])
        for n in range(self.window_size):
            for i in range(self.num_input):
                for j in range(self.num_hidden):
                    self.hiddenW[n*self.window_size + i, j] = np.random.uniform(-0.3, 0.3)

        # initialize weights between hidden layer and output layer
        self.outputW = np.zeros([self.num_hidden, self.num_output])
        for j in range(self.num_hidden):
            for k in range(self.num_output):
                self.outputW[j, k] = np.random.uniform(-0.3, 0.3)


    """
    Initialize network units to 0s.
    """
    def initializeUnits(self):
        # initialize input units for the size of the window we will be using
        self.input_units = []
        for n in range(self.window_size):
            for i in range(self.num_input):
                self.input_units.append(0.0)

        # initialize hidden units
        self.hidden_units = []
        for j in range(self.num_hidden):
            self.hidden_units.append(0.0)

        # initialize output units for a single phoneme
        self.output_units = []
        for k in range(self.num_output):
            self.output_units.append(0.0)


    """
    Train the network on the examples from NetTalk.
    I might possible need to add iterations?
    """
    def train_network(self):
        for t in range(self.iterations):
            hidden_totals = np.zeros([self.window_size*self.num_input, self.num_hidden])
            output_totals = np.zeros([self.num_hidden, self.num_output])
            for example in self.data:
                word = example[0]
                pron = example[1]
                letters = list(word)
                sounds = list(pron)

                # hidden_totals = np.zeros([self.window_size*self.num_input, self.num_hidden])
                # output_totals = np.zeros([self.num_hidden, self.num_output])

                # for each letter in the word, perform forward propagation to calculate
                # the error and deltas for each letter, which will be added up for
                # the whole word itself
                for l in range(len(letters)):
                    window = []
                    inclusive = l - ((self.window_size - 1)/2)
                    exclusive = l + ((self.window_size - 1)/2) + 1
                    for x in range(inclusive, exclusive):
                        if x < 0 or x > (len(letters) - 1):
                            window.append('_')
                        else:
                            window.append(letters[l])
                    output_delta_update, hidden_delta_update = self.get_letter_prediction(window, sounds[l])
                    for n in range(self.window_size):
                        for i in range(self.num_input):
                            for j in range(self.num_hidden):
                                index = n*self.window_size + i
                                hidden_totals[index, j] += hidden_delta_update[index, j]
                    for j in range(self.num_hidden):
                        for k in range(self.num_output):
                            output_totals[j, k] += output_delta_update[j, k]

            # now perform the weight updates after the whole word has been processed
            for n in range(self.window_size):
                for i in range(self.num_input):
                    for j in range(self.num_hidden):
                        index = n*self.window_size + i
                        old_weight = self.hiddenW[index, j]
                        self.hiddenW[index, j] = old_weight + self.learning_rate*(hidden_totals[index, j]/float(len(self.data)))
            for j in range(self.num_hidden):
                for k in range(self.num_output):
                    old_weight = self.outputW[j, k]
                    self.outputW[j, k] = old_weight + self.learning_rate*(output_totals[j, k]/float(len(self.data)))


    """
    Get the network's prediction for an example.
    """
    def get_letter_prediction(self, window, p):
        self.initializeUnits()

        output_deltas = []
        for k in range(self.num_output):
            output_deltas.append(0.0)
        hidden_deltas = []
        for j in range(self.num_hidden):
            hidden_deltas.append(0.0)

        # fix active units in the input
        for n in range(self.window_size):
            letter = window[n]
            index = self.getIndexForLetter(letter)
            self.input_units[n*self.window_size + index] = 1.0

        # propagate activation through the network
        for j in range(self.num_hidden):
            activation = 0
            for n in range(self.window_size):
                for i in range(self.num_input):
                    index = n*self.window_size + i
                    activation += self.hiddenW[index, j]*self.input_units[index]
            self.hidden_units[j] = self.sigmoid(activation)
        for k in range(self.num_output):
            activation = 0
            for j in range(self.num_hidden):
                activation += self.outputW[j, k]*self.hidden_units[j]
            self.output_units[k] = self.sigmoid(activation)

        # calculate error and backpropagation
        active = self.getIndexForPhoneme(p)
        for k in range(self.num_output):
            output_deltas[k] = self.output_units[k]*(1 - self.output_units[k])
            if k == active:
                if self.output_units[k] < 0.9:
                    output_deltas[k] += 1 - self.output_units[k]
                else:
                    output_deltas[k] += 0
            else:
                if self.output_units[k] > 0.1:
                    output_deltas[k] += 0 - self.output_units[k]
                else:
                    output_deltas[k] += 0
        for j in range(self.num_hidden):
            hidden_deltas[j] = self.hidden_units[j]*(1 - self.hidden_units[j])
            backprop = 0
            for k in range(self.num_output):
                backprop += output_deltas[k]*self.outputW[j, k]
            hidden_deltas[j] *= backprop

        # store values to be summed over for the word
        hiddens = np.zeros([self.window_size*self.num_input, self.num_hidden])
        outputs = np.zeros([self.num_hidden, self.num_output])

        for j in range(self.num_hidden):
            for k in range(self.num_output):
                outputs[j, k] = output_deltas[k]*self.hidden_units[j]
        for n in range(self.window_size):
            for i in range(self.num_input):
                index = n*self.window_size + i
                for j in range(self.num_hidden):
                    hiddens[index, j] = hidden_deltas[j]*self.input_units[index]

        return outputs, hiddens


    """
    Get the accuracy of the network by testing it on the test data.
    """
    def test_network(self):
        num_correct = 0
        correctletters = 0
        for example in self.test_data:
            correct = True

            word = example[0]
            pron = example[1]
            letters = list(word)
            sounds = list(pron)

            # for each letter in the word, perform forward propagation to calculate
            # the error and deltas for each letter, which will be added up for
            # the whole word itself
            printletters = []
            for l in range(len(letters)):
                correctletter = True
                window = []
                inclusive = l - ((self.window_size - 1)/2)
                exclusive = l + ((self.window_size - 1)/2) + 1
                for x in range(inclusive, exclusive):
                    if x < 0 or x > (len(letters) - 1):
                        window.append('_')
                    else:
                        window.append(letters[l])
                self.initializeUnits()
                # fix active units in the input
                for n in range(self.window_size):
                    letter = window[n]
                    index = self.getIndexForLetter(letter)
                    self.input_units[n*self.window_size + index] = 1.0

                # propagate activation through the network
                for j in range(self.num_hidden):
                    activation = 0
                    for n in range(self.window_size):
                        for i in range(self.num_input):
                            index = n*self.window_size + i
                            activation += self.hiddenW[index, j]*self.input_units[index]
                    self.hidden_units[j] = self.sigmoid(activation)
                for k in range(self.num_output):
                    activation = 0
                    for j in range(self.num_hidden):
                        activation += self.outputW[j, k]*self.hidden_units[j]
                    self.output_units[k] = self.sigmoid(activation)

                # index that should be active
                active = self.getIndexForPhoneme(sounds[l])
                desired = 0
                maximum = 0
                for k in range(self.num_output):
                    print str(k) + ": " + str(self.output_units[k])
                    if k == active:
                        # if self.output_units[k] < 0.9:
                        #     # correctletter = False
                        #     # correct = False
                        desired = self.output_units[k]
                    else:
                        # if self.output_units[k] > 0.1:
                        #     # correctletter = False
                        if self.output_units[k] > maximum:
                            maximum = self.output_units[k]
                            # correct = False
                if desired <= maximum:
                    correctletter = False
                    correct = False
                if correctletter:
                    correctletters += 1
                    printletters.append(letters[l])

            if correct:
                num_correct += 1
                print 'CORRECT'

        accuracy = float(num_correct)/float(len(self.test_data))
        print 'STATS'
        print 'Accuracy (' + str(num_correct) + '/' + str(len(self.test_data)) + '): ' + str(accuracy)
        print 'correct letters: ' + str(correctletters)
        print printletters


    """
    Return the index in the input arrays for a particular letter.
    """
    def getIndexForLetter(self, letter):
        return (ord(letter) - ord('a'))


    """
    Return the index in the output array for a particular phoneme.
    """
    def getIndexForPhoneme(self, phoneme):
        return {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'k': 9,
            'l': 10, 'm': 11, 'n': 12, 'o': 13, 'p': 14,
            'r': 15, 's': 16, 't': 17, 'u': 18, 'v': 19,
            'w': 20, 'x': 21, 'y': 22, 'z': 23, 'A': 24,
            'C': 25, 'D': 26, 'E': 27, 'G': 28, 'I': 29,
            'J': 30, 'K': 31, 'L': 32, 'M': 33, 'N': 34,
            'O': 35, 'Q': 36, 'R': 37, 'S': 38, 'T': 39,
            'U': 40, 'W': 41, 'X': 42, 'Y': 43, 'Z': 44,
            '@': 45, '!': 46, '#': 47, ':': 48, '^': 49,
            '+': 50, '*': 51, '-': 52
        }[phoneme]

    """
    Return the letter for a particular index in the input arrays.
    """
    def getLetterForIndex(self, index):
        return chr(index + ord('a'))


    """
    Return the phoneme for a particular index in the output array.
    """
    def getPhonForIndex(self, index):
        return 'X'


    """
    Return the squashed activation.
    """
    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))
