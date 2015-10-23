import lib, glob, commands, os, operator, pickle

folder = "../image/5k_75"
fs = glob.glob(folder + "/*.jpg")

mask = 16

def encode(s):
	r = ""
	for i in range(1, mask + 1):
		if s[i] != "0":
			r += "1"
		else:
			r += "0"
	return r

res = {}
for f in fs:
	print f
	if not os.path.isfile(f + ".block"):
		commands.getstatusoutput("/opt/libjpeg-turbo-coef/bin/jpegtran -outputcoef %s %s temp.jpg"%(f + ".block", f))
	
	ls = open(f + ".block").readlines()
	
	for l in ls:
		s = l.split(":")
		if s[0] != "0":
			continue
		
		ss = s[1][1:].split(" ")
		c = encode(ss)
		if c in res:
			res[c] += 1
		else:
			res[c] = 1
		
sort = sorted(res.items(), key=operator.itemgetter(1), reverse = True)
print sort[:100]
print res["0000000000000000"]
pickle.dump(sort, "hist_binary.pickle")

