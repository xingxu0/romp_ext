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

saving = 0.15
y_gain = []
y_overhead = []
y_overall = []
y_gain2 = []


i_ = [10, 100, 1000, 1000000, 1000000000]

for i in i_:
	b = i*290.0/1000
	x.append(i)
	j.append(i*290.0/1000/b)
	r.append(i*290.0*(1-saving)/1000/b)
	t.append(7.0/b)
print j
print r
f = plt.figure()
ax = plt.subplot(111)

bar_d = 0.3
d = bar_d/6
log_ = False
l_x = []
r_x = []
for i in range(len(i_)):
	l_x.append(i - d - bar_d)
	r_x.append(i + d)
	
ax.bar(l_x, j, edgecolor='k',color='#f3f3f3', width=bar_d, log=log_)
ax.bar(r_x, t, hatch='/', edgecolor='r',color='none', width=bar_d, log=log_)
ax.bar(r_x, r, hatch='\\', edgecolor='b',color='none', width=bar_d, log=log_, bottom=t)

for i in range(len(i_)):
	print i, j[i],r[i],t[i]
	s = 0
	if -r[i]-t[i]+j[i] > 0:
		s = int(round((-r[i]-t[i]+j[i])*100.0/j[i]))
	y = 0.03 + (r[i] + t[i])
	if y > 1.5:
		y=1.4
	ax.text(r_x[i], y, str(s)+"%",  fontsize=24)

#ax.bar(range(len(i_)), y_overhead, hatch='\\',edgecolor='r',color='none', width=0.6)
#ax.set_ylim(10, 20)  # outliers only
#ax.set_xlim(-0.2, 3.8)  # most of the data
ax.legend(["JPEG", "ROMP-Table", "ROMP-Image"], 1, fontsize = legend_font_size)
ax.set_xticks(range(len(i_)))
s = []
for i in i_:
	s.append(r"$10^%d$"%(int(round(math.log(i, 10)))))
ax.set_xticklabels(s)

ax.set_xlabel('Number of Photos', fontsize = label_font_size)
ax.set_ylabel('Size (MB)', fontsize = label_font_size)
ax.set_xlim(l_x[0]-0.5+bar_d, r_x[len(r_x)-1]+0.5)  # most of the data
ax.set_ylim(0, 1.6)
ax.tick_params(axis='x', pad=8)
#ax.set_yticks([])

#if log_:
#	ax.set_yscale('log')
set_ax(ax)
set_plt(plt)
plt.tick_params(axis='x', which='major', labelsize=25)

plt.savefig('jpeg_vs_romp_3.png')
plt.savefig('jpeg_vs_romp_3.eps')
plt.close()
