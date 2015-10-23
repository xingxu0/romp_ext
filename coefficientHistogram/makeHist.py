#!/usr/bin/python

import os
import numpy as np
from os import listdir
import matplotlib.pyplot as plt
from os.path import isfile, join

files = [ f for f in listdir('./') if isfile(join('./',f)) and f.endswith('.out')]

count = 0
ind = 0
freq = np.zeros((64))
x = np.arange(64)

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

ax = plt.subplot()
ax.bar(x,freq,width=0.2,color='r',align='center')
plt.xlabel('EOB position')
plt.ylabel('Frequency')
plt.show()
plt.savefig('hist.png')
# print files