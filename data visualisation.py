# Import 'numpy' module from installed path
import numpy as np
# Import 'matplotlib' module from installed path
import matplotlib.pyplot as plt
# Import colors from 'matplotlib'
from matplotlib import cm
import csv

# set maximum modularity class
MAX = 10
# create random colors
cs=cm.gist_ncar(np.arange(0, 500, 20))

# # open dataset file
# with open('dataset.csv') as f:
# 	# initialize empty array of shape(MAX, 2)
# 	A_bar = np.zeros(shape=(MAX, 2))
# 	# read file line by line
# 	for row in f:
# 		# split line seperated by comma
# 		labels = row[:-1].split(',')
# 		break
# 	print labels
# 	# create data list
# 	data = []
# 	reader = csv.reader(f)
# 	for line in reader:
# 		# split again
# 		row = line
# 		print row
# 		# create label dictionary
# 		temp = {}
# 		# read file again
# 		for i in range(len(row)):
# 			# insert into dictionary
# 			temp[labels[i]] = row[i]
# 		# append into array
# 		data.append(temp)

# function to plot stack histogram
def plot_hist(data):
	# initialize empty array of shape(MAX, 2)
	A_bar = np.zeros(shape=(MAX, 2))
	# read data file
	for rdata in data:
		try:
			# try to create stack histogram data
			group = int(rdata['group']) - 1
			# get modularity class
			modularity = int(rdata['modularity_class'])
			# insert into data
			A_bar[modularity][group] = 1 + A_bar[modularity][group]
		# what if we caught an exception ?
		except Exception as e:
			# pass it! I don't care
			pass
	# we have 2 classes
	X = range(2)
	# iterate over all classes
	for i in range(MAX):
		# with None
		bottom = None
		# do stack handling
		if i != 0:
			# Yeah that
			bottom = A_bar[i - 1]
		# create bar for each class
		plt.bar(X, A_bar[i], color = cs[i], bottom = bottom)
	# show the plot
	plt.show()

# function to plot pie chart
def pie_chart(data):
	# create categories dictionaries
	categories = [{}, {}]
	# read data
	for rdata in data:
		# find category
		category = rdata['category']
		# to handle different colors issue
		if category not in categories[0]:
			# make fake entries with 0 values
			categories[0][category] = 0
			# yeah for both the network
			categories[1][category] = 0
	# read data again. Yeah again!
	for rdata in data:
		# fetch group number
		group = int(rdata['group']) - 1
		# fetch category name
		category = rdata['category']
		# increment counter
		categories[group][category] = 1 + categories[group][category]
	# create figure
	fig = plt.figure()
	# divide it into sections 1x3 matrix
	ax1 = fig.add_subplot(131)
	# select first cell and plot first pie
	ax1.pie(categories[0].values(), labels=categories[0].keys(), startangle=90, colors=cs)
	# this is required to plot circular shape
	ax1.axis('equal')
	# select third cell
	ax1 = fig.add_subplot(133)
	# plot second pie
	ax1.pie(categories[1].values(), labels=categories[1].keys(), startangle=90, colors=cs)
	# this is required to plot circular shape
	ax1.axis('equal')
	# pack layout
	plt.tight_layout()
	# showm grapb
	plt.show()

# are we running directly from terminal ?
if __name__ == '__main__':

	# open dataset1.csv file
	with open('dataset3.csv','r') as f:
		for row in f:
			# get labels from csv
			labels = row[:-1].split(',')
			break
		labels.append('group')
		#create data dictionary
		data = []
		# read file line by line
		reader=csv.reader(f)
		for line in reader:
			# split line seperated by comma
			row = line
			# create label dictionary
			temp = {}
			# read file again
			for i in range(len(row)):
				try:
					# insert into dictionary
					temp[labels[i]] = row[i]
				except:
					print row
					pass
				# set group as 1
				temp['group'] = 1
				# add into data
				data.append(temp)
	# close file
	f.close()
	print"done dataset1"
	# open dataset2.csv file
	with open('dataset4.csv','r') as f:
		reader = csv.reader(f)
		for line in reader:
			# read file line by line
			row = line
			# split line seperated by comma
			temp = {}
			# create label dictionary
			for i in range(len(row)):
				# read file again
				try:
					# add into dictionary
					temp[labels[i]] = row[i]
				except:
					print row
					pass
				# set group as 2
				temp['group'] = 2
				# add into data
				data.append(temp)
	# close file
	f.close()
	print"done dataset2"
	# write into dataset.cdv file
	with open('dataset.csv','w') as f:
		# write labels into file
		f.write(','.join(labels))
		f.write('\n')
		for i in range(len(data)):
			# create list
			temp=[]
			for label in labels:
				# insert into list in the order of labels
				temp.append(str(data[i][label]))
			# write into file
			f.write(','.join(temp))
			f.write('\n')
	# close file
	f.close()
	print"done"

	# Yes
	pie_chart(data)

	# Yes
	plot_hist(data)
