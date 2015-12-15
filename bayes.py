import sys

p_y = {}
p_yi_w0 = {}
p_yi_w1 = {}
p_yi_w2 = {}
p_yi_w3 = {}
p_yi_w_1 = {}
p_yi_w_2 = {}
p_yi_w_3 = {}
total = 0
alpha = 1.0

def pys():
  with open(sys.argv[1]) as f:
    for line in f:
	a = line.split()
	if (len(a) > 1):
  	  one = len(a[0])
  	  two = len(a[1])
	  if (one == two) :
		a1 = "_" + a[1] + "_"
	        for c in a1:
		    if (p_y.has_key(c)):
			p_y[c] = p_y[c] + 1.0
		    else:
			p_y[c] = 1.0
  num = 0
  for v in p_y.values():
    num = num + v
  return num



def upPYiW0(word, phon):
  for i in range(0, len(phon)):
	y = phon[i]
	w0 = word[i]
	key = y + w0
	if (p_yi_w0.has_key(key)):
	  p_yi_w0[key] = p_yi_w0[key] + 1.0
        else:
 	  p_yi_w0[key] = 1.0

def upPYiW1(word, phon):
  for i in range(0, len(phon) - 1):
	y = phon[i]
	w0 = word[i + 1]
	key = y + w0
	if (p_yi_w1.has_key(key)):
	  p_yi_w1[key] = p_yi_w1[key] + 1.0
        else:
 	  p_yi_w1[key] = 1.0

def upPYiW_1(word, phon):
  for i in range(1, len(phon)):
	y = phon[i]
	w0 = word[i - 1]
	key = y + w0
	if (p_yi_w_1.has_key(key)):
	  p_yi_w_1[key] = p_yi_w_1[key] + 1.0
        else:
 	  p_yi_w_1[key] = 1.0


def upPYiW_2(word, phon):
  for i in range(2, len(phon)):
	y = phon[i]
	w0 = word[i - 2]
	key = y + w0
	if (p_yi_w_2.has_key(key)):
	  p_yi_w_2[key] = p_yi_w_2[key] + 1.0
        else:
 	  p_yi_w_2[key] = 1.0


def upPYiW_3(word, phon):
  for i in range(3, len(phon)):
	y = phon[i]
	w0 = word[i - 3]
	key = y + w0
	if (p_yi_w_3.has_key(key)):
	  p_yi_w_3[key] = p_yi_w_3[key] + 1.0
        else:
 	  p_yi_w_3[key] = 1.0


def upPYiW2(word, phon):
  for i in range(0, len(phon) - 2):
	y = phon[i]
	w0 = word[i + 2]
	key = y + w0
	if (p_yi_w2.has_key(key)):
	  p_yi_w2[key] = p_yi_w2[key] + 1.0
        else:
 	  p_yi_w2[key] = 1.0



def upPYiW3(word, phon):
  for i in range(0, len(phon) - 3):
	y = phon[i]
	w0 = word[i + 3]
	key = y + w0
	if (p_yi_w3.has_key(key)):
	  p_yi_w3[key] = p_yi_w3[key] + 1.0
        else:
 	  p_yi_w3[key] = 1.0


def getProd(str, y):
	ny = p_y[y]
	nyi = 0.0
	key = y + str[3]
	if (p_yi_w0.has_key(key)):
	  nyi = p_yi_w0[key]      
	w0 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	nyi = 0.0
	key = y + str[4]
	if (p_yi_w1.has_key(key)):
	  nyi = p_yi_w1[key]      
	w1 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	nyi = 0.0
	key = y + str[2]
	if (p_yi_w_1.has_key(key)):
	  nyi = p_yi_w_1[key]      
	w_1 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	nyi = 0.0
	key = y + str[1]
	if (p_yi_w_2.has_key(key)):
	  nyi = p_yi_w_2[key]      
	w_2 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	nyi = 0.0
	key = y + str[0]
	if (p_yi_w_3.has_key(key)):
	  nyi = p_yi_w_3[key]      
	w_3 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	nyi = 0.0
	key = y + str[5]
	if (p_yi_w2.has_key(key)):
	  nyi = p_yi_w2[key]      
	w2 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	nyi = 0.0
	key = y + str[6]
	if (p_yi_w3.has_key(key)):
	  nyi = p_yi_w3[key]      
	w3 = (nyi + alpha) / (ny + (alpha * 26 * 7))
	return (w0 * w1 * w2 * w3 * w_1 * w_2 * w_3)



def pred(word):
  pron = ""
  temp = "___" + word + "___"
  for i in range(0, len(word)):
    w = word[i]
    str = temp[i] + temp[i+1] + temp[i + 2] + temp[i+3] + temp[i + 4] + temp[i + 5] + temp[i + 6]
    yhat = "_"
    yval = 0.0
    for y in p_y.keys():
	ny = p_y[y]
	py = ny / total
	prod = getProd(str, y)
	v = py * prod
	if (v > yval):
	  yval = v
	  yhat = y
    pron = pron + yhat
  print word, ": ", pron
  return pron


total = pys()

with open(sys.argv[1]) as f:
    for line in f:
	a = line.split()
	if (len(a) > 1):
  	  one = len(a[0])
  	  two = len(a[1])
	  if (one == two) :
		a[0] = "_" + a[0] + "_"
		a[1] = "_" + a[1] + "_"
		upPYiW0(a[0], a[1])
		upPYiW1(a[0], a[1])
		upPYiW_1(a[0], a[1])
		upPYiW_2(a[0], a[1])
		upPYiW_3(a[0], a[1])
		upPYiW2(a[0], a[1])
		upPYiW3(a[0], a[1])

end = 0.0
right = 0.0
pend = 0.0
pright = 0.0


#pred("ape")
with open(sys.argv[2]) as f:
    for line in f:
	a = line.split()
	if (len(a) > 1):
  	  one = len(a[0])
  	  two = len(a[1])
	  if (one == two) :
		pron = pred(a[0])
                if (pron == a[1]):
		  right = right + 1.0
		end = end + 1.0
		for i in range(0, len(pron)):
		  if pron[i] == a[1][i]:
			pright = pright + 1.0
		  pend = pend + 1.0
print "Word accuracy:", (right / end)
print "Phoneme accuracy:", (pright / pend)
