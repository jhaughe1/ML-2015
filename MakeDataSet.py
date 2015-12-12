import random

def makeDataSetPair(datafile):
    f = open(datafile, 'r')

    examples = []
    examples2 = []

    randomlines = random.sample(xrange(12, 20000), 1000)
    randomlines2 = random.sample(xrange(12, 20000), 1000)
    i = 0

    for line in f:
        store = line
        line.strip()
        example = line.split()

        if len(example) == 3 or len(example) == 4:
            if randomlines.count(i) > 0:
                    examples.append(store)

            if randomlines2.count(i) > 0:
                examples2.append(store)

        i += 1

    f.close()

    f1 = open('random_1000_train.txt', 'w')
    f2 = open('random_1000_test.txt', 'w')

    for example in examples:
        f1.write(example)

    for example in examples2:
        f2.write(example)

    f1.close()
    f2.close()

makeDataSetPair('nettalk.data.txt')
