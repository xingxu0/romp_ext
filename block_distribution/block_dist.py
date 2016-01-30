import lib, glob, commands, os, operator, pickle, sys
from os.path import isfile, join
from os import listdir
import matplotlib.pyplot as plt
import math

if len(sys.argv) <= 1:
	print "Improper usage: python hist_binary.py <path to directory>"
	sys.exit()

folder = sys.argv[1]
print folder
# folder = "../image/5k_75"
# folder = "../image/tecnick_1200_75"
# fs = glob.glob(folder + "/*.jpg")

MASK = 16

code = lib.get_luminance_codes()

def encode(s):
	r = ""
	for i in range(1, 64):
		r += str(s[i]) + " "
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
res2= {}
total = 0

files = glob.glob(folder + "/*.jpg")

for f in files:
	os.system("/opt/libjpeg-turbo-coef/bin/jpegtran -outputcoef temp.out %s temp.out2"%(f))
	with open("temp.out",'r') as infile:
		for line in infile:
			dccoef = line.split(":")
			if dccoef[0] != "0":
				continue

			c_ = dccoef[1].split(" ")
			coef = []
			for x in c_:
				try:
					coef.append(lib.get_bits(abs(int(x))))
				except ValueError:
					pass
			c = encode(coef)
			total += 1
			b = lib.get_jpeg_bits(coef, 1, 63, code, True)[0]
			if b>50:
				continue
			if c in res:
				res[c] += 1
			else:
				#b = lib.get_jpeg_bits(coef, 1, 63, code, True)[0]
				res[c] = 1
				#res2[c] = b
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
#sort = sorted(res.items(), key=operator.itemgetter(1), reverse = True)
#for x_ in sort:
#	x = x_[0]
#	p = res[x]*1.0/total
#	print x, res[x], res2[x], res[x]*1.0/total, math.log(1.0/p, 2) 

output = open("block_dist.pickle", "wb")
pickle.dump(res, output)
output.close()

#output2 = open("block_dist_jpeg.pickle", "wb")
#pickle.dump(res2, output2)
#output2.close()
