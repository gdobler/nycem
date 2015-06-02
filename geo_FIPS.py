import os 
import json
from urllib import urlopen 
import csv 
from datetime import datetime

def load_MI_data(file):
	f = open(file) 
	reader = csv.reader(f) 

	median_incomes = {} 
	headers = reader.next() 
	ct_index = headers.index('Geo_TRACT') 

	for item in reader: 
		cbt = item[18] + item[19] 
		try:
			mi = float(item[ct_index])
			median_incomes[cbt] = mi 
		except:
			mi = 0 
			median_incomes[cbt] = 0 

	print median_incomes
					
def load_refUSA_data(file, otherdata):
	f = open(file) 
	reader = csv.reader(f)
	headers = reader.next() 
	
	co_name = headers.index('CONAME')
	co_add = headers.index('ADDR') 
	ct = headers.index('CENSUS_TRACT_2010') 
	cb = headers.index('CENSUS_BG_2010') 

	for business in reader:
		new_key = business[ct] + business[cb]
		
		try:
			print otherdata[new_key] 
		except:
			print 'nothing here' 

if __name__=='__main__':
	directory = os.environ['data_path']
	files = sorted(os.listdir(directory))
	df10 = directory + "/" + files[0] #make this dynamic at some point 
	load_MI_data("nys_mi.csv") 
	#load_refUSA_data(df10, mi) 
