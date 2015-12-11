"""
Phoneme Feature Accuracy Measurer
"""
from collections import Counter

class PhonemeFeatures:

    def __init__(self):
        self.correctFeatures = []       # number of times feature is in desired output
        self.matchingFeatures = []      # number of times feature is in actual output
        self.allFeatures = []           # all features that appear in the data

        self.features = {
            'a': ['vowel', 'open', 'central'],                                         # wad, dot, odd
            'b': ['consonant', 'bilabial', 'stop', 'voiced'],       # bad
            'c': ['vowel', 'unrounded', 'open', 'back'],             # caught, awe
            'd': ['consonant', 'alveolar', 'stop', 'voiced'],         # add
            'e': ['vowel', 'unrounded', 'mid', 'front'],             # blade, way
            'f': ['consonant', 'labiodental', 'fricative', 'voiceless'],         # farm
            'g': ['consonant', 'velar', 'stop', 'voiced'],         # gap
            'h': ['consonant', 'glottal', 'fricative', 'voiceless'],         # hot, who
            'i': ['vowel', 'unrounded', 'close', 'front'],             # eve, theme, bee
            'k': ['consonant', 'velar', 'stop', 'voiceless'],         # cab, keep
            'l': ['consonant', 'alveolar', 'lateral', 'voiced'],         # lad
            'm': ['consonant', 'bilabial', 'nasal', 'voiced'],         # man, imp
            'n': ['consonant', 'alveolar', 'nasal', 'voiced'],         #
            'o': ['vowel', 'rounded', 'mid', 'back'],             # only, own
            'p': ['consonant', 'bilabial', 'stop', 'voiceless'],         # pad, apt
            'r': ['consonant', 'alveolar', 'retroflex', 'voiced'],      # rap
            's': ['consonant', 'alveolar', 'fricative', 'voiceless'],         # cent, ask
            't': ['consonant', 'alveolar', 'stop', 'voiceless'],         # tab
            'u': ['vowel', 'rounded', 'close', 'back'],             # boot, oose, you
            'v': ['consonant', 'labiodental', 'fricative', 'voiced'],         # vat
            'w': ['consonant', 'bilabial', 'glide', 'voiced'],         # we, liquid
            'x': ['vowel', 'rounded', 'mid', 'front'],             # piRATE, welCOME
            'y': ['consonant', 'palatal', 'glide', 'voiced'],         # yes, senior
            'z': ['consonant', 'alveolar', 'fricative', 'voiced'],         # zoo, goes
            'A': ['vowel', 'unrounded', 'open', 'front'],             # ice, height, eye
            'C': ['consonant', 'alveopalatal', 'affricate', 'voiceless'],         # chart, cello
            'D': ['consonant', 'interdental', 'fricative', 'voiced'],         # the, mother
            'E': ['vowel', 'unrounded', 'mid', 'front'],             # many, end, head
            'G': ['consonant', 'velar', 'nasal', 'voiced'],         # length, long, bank
            'I': ['vowel', 'unrounded', 'mid', 'front'],             # give, BUsy, capTAIN
            'J': ['consonant', 'alveopalatal', 'affricate', 'voiced'],         # jam, gem
            'K': ['consonant', 'velar', 'stop', 'voiceless'],         # anxious
            'L': ['consonant', 'alveolar', 'lateral', 'voiced'],         # evil
            'M': ['consonant', 'bilabial', 'nasal', 'voiced'],         # chasm
            'N': ['consonant', 'alveolar', 'nasal', 'voiced'],         # shorten
            'O': ['vowel'],             # oil, boy
            'Q': ['consonant'],     # quilt
            'R': ['consonant', 'alveolar', 'retroflex', 'voiced'],                    # honer, satyr
            'S': ['consonant', 'postalveolar', 'fricative', 'voiceless'],           # ocean
            'T': ['consonant', 'interdental', 'fricative', 'voiceless'],            # thaw, bath
            'U': ['vowel', 'mid', 'back'],             # wood, could, put
            'W': ['vowel'],             # out, towel, house
            'X': ['consonant'],                # mixture, annex
            'Y': ['vowel'],                # use, feud, new
            'Z': ['consonant', 'postalveolar', 'fricative', 'voiced'],                   # usual, vision
            '@': ['vowel', 'unrounded', 'mid', 'front'],                # cab, plaid
            '!': ['consonant'],                # nazi, pizza
            '#': ['consonant'],                # auxiliary, exist
            ':': ['consonant'],                # what
            '^': ['vowel'],                # up, son, blood
            '+': ['vowel'],                # madmemoiselle
            '*': ['consonant', 'bilabial', 'glide', 'voiced'],                #
            '-': []             # nothing
        }

    def getFeaturesForPhoneme(self, phoneme):
        return self.features[phoneme]

    def addPhonemesToCount(self, predicted, desired):
        predicted_features = self.getFeaturesForPhoneme(predicted)
        desired_features = self.getFeaturesForPhoneme(desired)

        for feature in desired_features:
            self.correctFeatures.append(feature)
            if feature not in self.allFeatures:
                self.allFeatures.append(feature)

        for feature in predicted_features:
            if feature in desired_features:
                self.matchingFeatures.append(feature)

    def evaluate(self):
        correct_counter = Counter(self.correctFeatures)
        match_counter = Counter(self.matchingFeatures)
        for feature in self.allFeatures:
            print 'Accuracy for feature ' + feature + ' (' + str(match_counter[feature]) + '/' + str(correct_counter[feature]) + '): ' + str(float(match_counter[feature])/float(correct_counter[feature]))
