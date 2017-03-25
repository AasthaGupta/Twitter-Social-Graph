# -*- coding: utf-8 -*-
# @Author: aastha
# @Date:   2017-03-25 13:00:24
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-03-25 13:38:52


import os
import glob

def create_weight_list(inputfiles):

	output_file=open("Datasets/weights.txt","w")
	output_file.write('Source;Target;Weight\n')
	followers = {}
	for filename in glob.glob(inputfiles):
		user = os.path.splitext(os.path.basename(filename))[0]
		count=0
		with open(filename) as f:
			count = sum(1 for line in f)
		followers[user]=count
	with open("Datasets/edges.txt") as edges:
		for edge in edges:
			user1=edge.split(";")[0]
			user2=edge.split(";")[1][:-1]
			if user1 not in followers :
				continue
			f1=followers.get(user1, 0)
			f2=followers.get(user2, 0)
			delta=abs(f1-f2)
			w=100.00/(1+delta)
			w=w*(1+min(f1,f2))
			output_file.write('{};{}\n'.format(edge[:-1], w))

create_weight_list("Datasets/*.dataset")
