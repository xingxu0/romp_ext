import lib, glob, commands, os, operator, pickle, sys
from os.path import isfile, join
from os import listdir
import matplotlib.pyplot as plt

if len(sys.argv) <= 1:
	print "Improper usage: python hist_binary.py <path to directory>"
	sys.exit()

folder = sys.argv[1]
print folder
# folder = "../image/5k_75"
# folder = "../image/tecnick_1200_75"
# fs = glob.glob(folder + "/*.jpg")

MASK = 16

def encode(s,mask):
	r = ""
	for i in range(1, mask+1):
		if s[i] != "0":
			r += "1"
		else:
			r += "0"
	return r

def filterBlock(coef, position):
	ind = 0
	for i in range(63,-1,-1):
		if coef[i] != '0':
			ind = i
			break
	if (ind) != position:
		return False
	return True

res = {}
total = 0
# for f in fs:
# 	print f
# 	if not os.path.isfile(f + ".out"):
# 		commands.getstatusoutput("/opt/libjpeg-turbo-coef/bin/jpegtran -outputcoef %s %s temp.jpg"%(f + ".out", f))

files = [ f for f in listdir(folder) if isfile(join(folder,f)) and f.endswith('.out')]

for f in files:
	with open(folder+"/"+f,'r') as infile:
		for line in infile:
			dccoef = line.split(":")
			if dccoef[0] != "0":
				continue

			coef = dccoef[1].split()
			#filter block here
			if not filterBlock(coef,MASK):
				continue
			c = encode(coef,MASK)
			total += 1
			if c in res:
				res[c] += 1
			else:
				res[c] = 1

		print total
	infile.close()
	
# ls = open(f + ".out").readlines()

# for l in ls:
	

# 	filterBlock(ss)
# 	# filter to only look for those blocks which have EOB at 16
# 	c = encode(ss)
# 	total += 1
# 	if c in res:
# 		res[c] += 1
# 	else:
# 		res[c] = 1

# print total
sort = sorted(res.items(), key=operator.itemgetter(1), reverse = True)

x = []
y = []
yy = []

i = 0
now = 0
for o in sort:
	i += 1
	x.append(i)
	now += o[1]
	y.append(now*1.0/total)
	yy.append(o[1]*1.0/total)

ax = plt.subplot()
ax.plot(x, y)
ax.set_xlim([1, 65536])
plt.xlabel('Patterns')
plt.ylabel('CDF (1)')
plt.savefig('CDF.png')
plt.close()

ax = plt.subplot()
ax.scatter(x, yy, s=1)
ax.set_xlim([1, 65536])
plt.xlabel('Patterns')
plt.ylabel('PDF (1)')
plt.savefig('PDF.png')

	

print sort[:100]
# print res["0000000000000000"]
output = open("hist_binary__.pickle", "wb")
pickle.dump(sort, output)

