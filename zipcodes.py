import csv 

def pullzipcodes(): 
	f = open('zips.csv') 
	reader = csv.reader(f)
	
	zips = [] 

	for i in reader:
		zips.append(i[0]) 
	 
	return zips	

