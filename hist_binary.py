import lib, glob, commands, os, operator, pickle
import matplotlib.pyplot as plt

folder = "../image/5k_75"
#folder = "../image/tecnick_1200_75"
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
total = 0
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
		total += 1
		if c in res:
			res[c] += 1
		else:
			res[c] = 1

print total
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
print res["0000000000000000"]
output = open("hist_binary__.pickle", "wb")
pickle.dump(sort, output)

