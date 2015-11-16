#run by python features.py y n y y n word1 word2 word3 .... wordN
#arg 1 y for features of length 1 n for no features of length 1
#arg 2 y for features of length 2 n for no features of length 2
#arg 3 y for features of length 3 n for no features of length 3
#arg 4 y for features of length 4 n for no features of length 4
#arg 5 y for features of length 5 n for no features of length 5
#prnts out argument and list of features
import sys

one = sys.argv[1]
two = sys.argv[2]
three = sys.argv[3]
four = sys.argv[4]
five = sys.argv[5]

args = sys.argv

args.pop(0) #pop name
args.pop(0) #pop one
args.pop(0) #pop two
args.pop(0) #pop three
args.pop(0) #pop four
args.pop(0) #pop five

for arg in args: 
    print arg
    chars = ['_'] + list(arg) + ['_']
    features = []
    if (one == "y"):
	features = features + list(arg)
    if (two == "y"):
	for i in range(0, len(chars) - 1):
	    features = features  + [chars[i] + chars[i+1]]
    if (three == "y"):
	for i in range(0, len(chars) - 2):
	    features = features  + [chars[i] + chars[i+1] + chars[i+2]]
    if (four == "y"):
	for i in range(0, len(chars) - 3):
	    features = features  + [chars[i] + chars[i+1] + chars[i+2] + chars[i+3]]
    if (five == "y"):
	for i in range(0, len(chars) - 4):
	    features = features  + [chars[i] + chars[i+1] + chars[i+2] + chars[i+3] + chars[i+4]]
    print features
