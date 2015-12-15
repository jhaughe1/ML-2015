import sys

p_y = {}
p_yi_w0 = {}
p_yi_w1 = {}
p_yi_w2 = {}
p_yi_w3 = {}
p_yi_w_1 = {}
p_yi_w_2 = {}
p_yi_w_3 = {}
total = {}
alpha = 0.0012
letters = []
phonemes = []

def init():
  with open(sys.argv[1]) as f:
    letters.append("_")
    for line in f:
        a = line.split()
        if (len(a) > 1):
          one = len(a[0])
          two = len(a[1])
          if (one == two) :
              for l in a[0]:
                if l not in letters:
                    letters.append(l)
              for p in a[1]:
                if p not in phonemes:
                    phonemes.append(p)
    for l in letters:
        for p in phonemes:
            key = p + "" + l
            p_yi_w0[key] = 1.0
            p_yi_w1[key] = 1.0
            p_yi_w2[key] = 1.0
            p_yi_w3[key] = 1.0
            p_yi_w_1[key] = 1.0
            p_yi_w_2[key] = 1.0
            p_yi_w_3[key] = 1.0

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


def probs():
  for i in p_yi_w0.keys():
    y = i[0]
    w = i[1]
    p = float(p_yi_w0[i]) / float(p_y[y])
    p_yi_w0[i] = p
  for i in p_yi_w1.keys():
    y = i[0]
    w = i[1]
    p = p_yi_w1[i] / p_y[y]
    p_yi_w1[i] = p
  for i in p_yi_w2.keys():
    y = i[0]
    w = i[1]
    p = p_yi_w2[i] / p_y[y]
    p_yi_w2[i] = p
  for i in p_yi_w3.keys():
    y = i[0]
    w = i[1]
    p = p_yi_w3[i] / p_y[y]
    p_yi_w3[i] = p
  for i in p_yi_w_1.keys():
    y = i[0]
    w = i[1]
    p = p_yi_w_1[i] / p_y[y]
    p_yi_w_1[i] = p
  for i in p_yi_w_2.keys():
    y = i[0]
    w = i[1]
    p = p_yi_w_2[i] / p_y[y]
    p_yi_w_2[i] = p
  for i in p_yi_w_3.keys():
    y = i[0]
    w = i[1]
    p = p_yi_w_3[i] / p_y[y]
    p_yi_w_3[i] = p


def predict(word, position, p):
    w0 = p + word[position]
    w1 = p + word[position + 1]
    w2 = p + word[position + 2]
    w3 = p + word[position + 3]
    w_1 = p + word[position - 1]
    w_2 = p + word[position - 2]
    w_3 = p + word[position - 3]
    p1 = 0.0
    p2 = 0.0
    p3 = 0.0
    p0 = 0.0
    p_1 = 0.0
    p_2 = 0.0
    p_3 = 0.0
    if w0 in p_yi_w0:
	p0 = p_yi_w0[w0]
    if w1 in p_yi_w1:
	p1 = p_yi_w1[w1]
    if w2 in p_yi_w2:
	p2 = p_yi_w2[w2]
    if w3 in p_yi_w3:
	p3 = p_yi_w3[w3]
    if w_1 in p_yi_w_1:
	p_1 = p_yi_w_1[w_1]
    if w_2 in p_yi_w_2:
	p_2 = p_yi_w_2[w_2]
    if w_3 in p_yi_w_3:
	p_3 = p_yi_w_3[w_3]
    y = p0 + p1 + p2 + p3 + p_1 + p_2 + p_3
#p_yi_w0[w0] + p_yi_w_1[w_1] + p_yi_w_2[w_2] + p_yi_w_3[w_3] + p_yi_w1[w1] + p_yi_w2[w2] + p_yi_w3[w3]
    return y



def iter(word, position, phon):
    max = 0.0
    hat = "_"
    for p in phonemes:
        y = predict(word, position, p)
        if max == 0.0:
            max = y
            hat = p
        if y > max:
            max = y
            hat = p
    if hat != phon:
#      print "here"
      p = phon
      w0 = p + word[position]
      w1 = p + word[position + 1]
      w2 = p + word[position + 2]
      w3 = p + word[position + 3]
      w_1 = p + word[position - 1]
      w_2 = p + word[position - 2]
      w_3 = p + word[position - 3]
      p = hat
      w0h = p + word[position]
      w1h = p + word[position + 1]
      w2h = p + word[position + 2]
      w3h = p + word[position + 3]
      w_1h = p + word[position - 1]
      w_2h = p + word[position - 2]
      w_3h = p + word[position - 3]
#      print "before: ", p_yi_w0[w0]
      change = alpha * (predict(word, position, hat) - predict(word, position, phon))
#      print change
      p_yi_w0[w0] = p_yi_w0[w0] + change
      p_yi_w1[w1] = p_yi_w1[w1] + change
      p_yi_w2[w2] = p_yi_w2[w2] + change
      p_yi_w3[w3] = p_yi_w3[w3] + change
      p_yi_w_1[w_1] = p_yi_w_1[w_1] + change
      p_yi_w_2[w_2] = p_yi_w_2[w_2] + change
      p_yi_w_3[w_3] = p_yi_w_3[w_3] + change
#      print "after: ", p_yi_w0[w0]





def predL(word, position):
    max = 0.0
    hat = "_"
    for p in phonemes:
        y = predict(word, position, p)
        if max == 0.0:
            max = y
            hat = p
        if y > max:
            max = y
            hat = p
#        print p + ": " + str(y)
#    print "ll    " + hat + ": " + str(max)
    return hat


def pred(word):
    wor = "___" + word + "___"
    res = ""
    for x in range(3, len(wor) - 3):
        res = res + predL(wor, x)
    return res


def iterWord(word, result):
    word = "___" + word + "___"
    result = "___" + result + "___"
    for x in range(3, len(word) - 3):
        iter(word, x, result[x])







init()
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

with open(sys.argv[1]) as f:
    for line in f:
        a = line.split()
        if (len(a) > 1):
          one = len(a[0])
          two = len(a[1])
          if (one == two) :
              iterWord(a[0], a[1])



end = 0.0
right = 0.0
pend = 0.0
pright = 0.0


#print pred("ape")
#print pred("bsjytriowpjfslkjvnkjnfkjdn")

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
