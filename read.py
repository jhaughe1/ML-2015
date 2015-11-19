import sys

p_y = {}
p_yi_w0 = {}
#p_yi_w1 = {}
#p_yi_w_1 = {}
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
	        for c in a[1]:
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


def pred(word):
  pron = ""
  for w in word:
    yhat = "_"
    yval = 0.0
    for y in p_y.keys():
	ny = p_y[y]
	py = ny / total
	key = y + w
	nyi = 0.0
	if (p_yi_w0.has_key(key)):
	  nyi = p_yi_w0[key]      
	prod = (nyi + alpha) / (ny + (alpha * 26))
	v = py * prod
	if (v > yval):
	  yval = v
	  yhat = key[0]
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
		upPYiW0(a[0], a[1])

end = 0.0
right = 0.0
pend = 0.0
pright = 0.0
with open(sys.argv[1]) as f:
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
