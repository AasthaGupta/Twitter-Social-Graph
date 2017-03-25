# -*- coding: utf-8 -*-
# @Author: amaneureka
# @Date:   2017-03-25 08:41:51
# @Last Modified by:   amaneureka
# @Last Modified time: 2017-03-25 12:12:11

import os
import glob
from sets import Set

def create_node_and_edge_list(inputfiles):
	nodes = Set()
	edges = []
	for filename in glob.glob(inputfiles):
		node_a = os.path.splitext(os.path.basename(filename))[0]
		nodes.add(node_a)
		#if len(nodes) > 3000:
		#	break
		with open(filename, 'r') as file:
			for line in file:
				node_b = line[:-1]
				nodes.add(node_b)
				edges.append([node_a, node_b])
	print 'dumping nodes...' + str(len(nodes))
	with open('Datasets/nodes.txt', 'w') as file:
		file.write('Id;Label\n')
		for node in nodes:
			file.write('{};{}\n'.format(node, node))
	print 'dumping edges...' + str(len(edges))
	with open('Datasets/edges.txt', 'w') as file:
		file.write('Source;Target\n')
		for edge in edges:
			file.write('{};{}\n'.format(edge[0], edge[1]))

create_node_and_edge_list("Datasets/*.dataset")