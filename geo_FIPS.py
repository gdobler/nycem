import os 
import json
from urllib import urlopen 
import csv 
from datetime import datetime

def add_geoFIPS(lat, lng):
	
	address = "http://data.fcc.gov/api/block/find?format=json&latitude="+ str(lat) + "&longitude=" + str(lng) + "&showall=true"
	url = urlopen(address).read() 
	result = json.loads(url) 
	geo_fips = str(result['Block'].values()[0])
	return geo_fips	 

def load_data(file):
	f = open(file) 
	reader = csv.reader(f)
	headers = reader.next() 
	
	loc_list = [] 

	for i in reader:
		loc = (i[20], i[21]) 
		#loc_list.append(loc)  	
		print loc



#	print "done in ", datetime.now() - startTime	


if __name__=='__main__':
	startTime = datetime.now()
#	print startTime
	directory = os.environ['data_path']
	files = sorted(os.listdir(directory))
	df10 = directory + "/" + files[0] #make this dynamic at some point 
	load_data(df10) 
