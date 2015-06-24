import csv
import numpy as np 
import matplotlib.pyplot as plt 

# {cluster: ([],[],..), ..}
datadict = {}



filename = '../zbp_just_nyc/zbp_small_clustered.csv'
f = open(filename, 'r')
csvReader = csv.reader(f)
for row in csvReader:
	cluster = row[15]
	datalist = [row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]]
	if cluster in datadict:
		datadict[cluster].append(datalist)  
	else:
		datadict[cluster] = datalist

for zip in datadict["1"]:
	plt.plot(zip,'-b', label='Cluster 1')

for zip in datadict["2"]:
	plt.plot(zip,'-r', label='Cluster 2')

for zip in datadict["3"]:
	plt.plot(zip,'-g', label='Cluster 3')

for zip in datadict["4"]:
	plt.plot(zip,'-y', label='Cluster 4')

plt.show()