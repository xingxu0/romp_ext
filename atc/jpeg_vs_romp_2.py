import os, sys, math
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

sys.path.insert(0, '/home/xing/research/')
from plot import *

ax = plt.subplot()
x = []
j = []
r = []
t = []
s = []

saving = 0.15
y_gain = []
y_overhead = []
y_overall = []
y_gain2 = []


i_ = []
tt = 100
for x_ in range(tt):
	i_.append(x_*9.0/tt)
print i_

for i in i_:
	n = float(pow(10,i))
	x.append(n)
	j.append(290.0)
	j_ = 290.0
	r_ = (7000.0+n*290.0*(1-saving))/n
	r.append(r_)
	s.append((j_-r_)*100.0/j_)
	t.append(7000.0*100.0/(r_*n))
print j
print r
print t
print s
f = plt.figure()
ax = plt.subplot(111)
ax2 = ax.twinx()

ax.plot(x, j, "--k", lw=3)
ax.plot([-1,-1], [-1,-1], ":k", lw=3)
ax.plot(x, r, "-k", lw=3)
ax.plot([-1,-1], [-1,-1], "-+b", lw=3, ms=5)
ax2.plot(x, s, ":k", lw=3)
ax2.plot(x, t, "-+b", lw=3, ms=5)

ax.set_xscale('log')
ax2.set_xscale('log')
ax.legend(["JPEG", "Saving", "ROMP", "Table"], 1, fontsize = legend_font_size, ncol=2)

#s = []
#for i in i_:
#	s.append(r"$10^%d$"%(int(round(math.log(i, 10)))))
#ax.set_xticklabels(s)

ax.set_xlabel('Number of Photos', fontsize = label_font_size)
ax.set_ylabel('Size (KB)', fontsize = label_font_size)
#ax.set_xlim(l_x[0]-0.5+bar_d, r_x[len(r_x)-1]+0.5)  # most of the data
#ax.tick_params(axis='x', pad=8)
#ax.set_yticks([])a

ax.set_ylim(0, 500)
ax2.set_ylim(0,100)
ax2.set_ylabel('Percent (100%)', fontsize=label_font_size)

#if log_:
#	ax.set_yscale('log')
set_ax(ax)
set_plt(plt)
plt.tick_params(axis='x', which='major', labelsize=25)

plt.savefig('jpeg_vs_romp_2.png')
plt.savefig('jpeg_vs_romp_2.eps')
plt.close()
