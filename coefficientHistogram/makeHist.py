#!/usr/bin/python

import os
import numpy as np
from os import listdir
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
from os.path import isfile, join

files = [ f for f in listdir('./') if isfile(join('./',f)) and f.endswith('.out')]

count = 0
ind = 0
freq = np.zeros((64))
x = np.arange(1,65)

for f in files:
	with open(f,'r') as infile:
		for line in infile:
			coef = line.split()
			for i in range(64,-1,-1):
				if coef[i] != '0':
					ind = i
					break
			freq[ind-1] = freq[ind-1] + 1
	infile.close()

total = np.sum(freq)
percentage = 100*np.divide(freq,total,dtype='double')
ax = plt.subplot()
ax.bar(x,percentage,width=0.2,color='r',align='center')
plt.xlabel('EOB position')
plt.ylabel('Frequency (%)')
#plt.show()
plt.savefig('hist.pdf')
# print files
