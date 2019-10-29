#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:16:26 2018

@author: yurio
"""

from __future__ import print_function
from future.utils import iteritems

import random
import request

# load template
def load(filename):
	return [i for i in open(filename)]

# ekstraksi trigram dan inserting ke dictionary
# (w1 , w3) sebagai key, [w2] sebagai values
def trigrams(template):
	trigrams={}
	for review in template:
		s = review.lower()
		tokens = s.split()
		for i in range(len(tokens) - 2):
			k = (tokens[i], tokens[i+2])
			if k not in trigrams:
				trigrams[k]=[]
			trigrams[k].append(tokens[i+1])
	return trigrams

# ubah middle-words ke vector probability 
def trigram_probabilities(trigrams):
	trigram_probabilities = {}
	for k , words in iteritems(trigrams):
		
		if len(set(words))>1:
			
			d = {}
			n = 0
			for w in words:
				if w not in d:
					d[w] = 0
				d[w] += 1
				n += 1
			for w , c , in iteritems(d):
				d[w] = float(c) / n
			trigram_probabilities[k] = d
	return trigram_probabilities

def random_sample(d):
	
	r = random.random()
	cumulative = 0
	for w , p in iteritems(d):
		cumulative += p
		if r < cumulative :
			return	w

def change_item(d,k):

	for w , p in iteritems(d):

		if w != k :
			return	w

def test_spinner():
	filename = 'template_20180509.txt'
	trigram_prob = trigram_probabilities(trigrams(load(filename)))
	review = random.choice(load(filename))
	s = review.lower()
	print("Original:", s)
	tokens = s.split()
	for i in range(len(tokens) - 2) :
		if random.random() < 1 : 
			k = (tokens[i], tokens[i+2])
			c = tokens[i+1] 
			if k in trigram_prob:
				w = change_item(trigram_prob[k],c)
				tokens[i+1] = w
	print("Spun")
	print(" ".join(tokens).replace(" .", ".").replace(" '","'").replace(" !","!").replace(" ,",","))

if __name__ == '__main__':
	test_spinner()

