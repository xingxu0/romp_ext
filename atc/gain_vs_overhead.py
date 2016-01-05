import os, sys
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

sys.path.insert(0, '/home/xing/research/')
from plot import *

ax = plt.subplot()
x = []
y_gain = []
y_overhead = []
y_overall = []
y_gain2 = []


i_ = [10, 100, 1000, 1000000000]

for i in i_:
	x.append(i)
	y_gain.append(i*290*.15/1000)
	y_overhead.append(-7)
	y_overall.append(i*290*.15/1000 - 7)
	i *= 2
y_gain[len(y_gain)-1] += 5
print y_gain
y_gain2 = [-10, -10, -10, 15]
#y_gain3 = [1, 1, 1, 0]

sc = 5
f = plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[1, sc]) 
ax = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
#ax = f.add_subplot(211)
#ax2 = f.add_subplot(212)
	
ax.bar(range(len(i_)), y_gain2, hatch='/',edgecolor='b',color='none', width=0.6)
ax.bar(range(len(i_)), y_overhead, hatch='\\',edgecolor='r',color='none', width=0.6)
#ax.bar(range(len(i_)), y_gain3, edgecolor="w", color='w',width=0.6)
#ax.bar(range(len(i_)), y_overhead, hatch='\\',edgecolor='r',color='none', width=0.6)

ax2.bar(range(len(i_)), y_gain, hatch='/',edgecolor='b',color='none', width=0.6)
ax2.bar(range(len(i_)), y_overhead, hatch='\\',edgecolor='r',color='none', width=0.6)

ax.set_ylim(10, 20)  # outliers only
ax2.set_ylim(-10, 50)  # most of the data
ax2.set_xlim(-0.2, 3.8)  # most of the data
ax.set_xlim(-0.2, 3.8)  # most of the data
ax2.legend(["Saving", "Overhead"], 2, fontsize = legend_font_size)

ax2.plot([-100, 100], [0,0], "-k")

ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d*sc, +d*sc), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d*sc, +d*sc), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

ax.yaxis.set_offset_position('left')
ax.yaxis.get_offset_text().set_size(22)
#ax.plot(x, y_overall)

ax.set_yticks([])
#ax.set_xscale('log')
#ax.set_yscale('log')
t = []
for x in range(len(i_)):
	t.append(x+0.3)
ax2.set_xticks(t)
ax2.set_xticklabels(i_)
ax2.set_xlabel('Number of Photos', fontsize = label_font_size)
ax2.set_ylabel('a', fontsize = label_font_size, color="w")
f.text(0.025, 0.55, 'Size (MB)', fontsize = label_font_size,  rotation="vertical", va="center")
f.text(0.055, 0.87, '~5e7', fontsize = label_size)
#f.text(0.06, 0.96, '~4e7', fontsize = label_size)


set_ax(ax)	
set_plt(plt)

plt.savefig('photo_number.png')
plt.savefig('photo_number.eps')
plt.close()