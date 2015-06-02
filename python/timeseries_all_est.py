import csv
import numpy as np 
import matplotlib.pyplot as plt 

datadict = {}
filename = 'NYC_zip_aggregates_by_year.csv'
with open(filename,'r') as f:
	csvReader = csv.reader(f)
	headers = csvReader.next()
	for row in csvReader:
		zip = row[0]
		est = int(row[2])
		year = int(row[12])
		if zip in datadict:
			datadict[zip][0].append(year)
			datadict[zip][1].append(est)
		else:
			datadict[zip] = [[year],[est]]

zdatadict = {}
for zip in datadict:
	zdatadict[zip] = [[],[]]
	raw = datadict[zip]
	mean = np.mean(raw[1])
	std = np.std(raw[1])
	for i in range(len(raw[0])):
		z = (raw[1][i]-mean)/std
		zdatadict[zip][0].append(raw[0][i])
		zdatadict[zip][1].append(z)

mean = [[],[]]
i = 1994
while i<2013:
	mean[0].append(i)
	sum = 0
	n = 0
	for zip in zdatadict:
		if i in zdatadict[zip][0]:
			index = zdatadict[zip][0].index(i)
			count = zdatadict[zip][1][index]
			sum += count
			n+=1
	mean[1].append(sum/n)

	i+=1

for i in zdatadict:
	plt.plot(zdatadict[i][0],zdatadict[i][1])
plt.plot(mean[0],mean[1],'k-',lw=3,label="mean")
plt.xlabel("year")
plt.ylabel('z')
plt.title("time series of establishment count by zip code normalized")
plt.legend()

plt.show()
