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

	for item in reader: 
		new_key = item[18] + item[19] 
		if len(new_key) == 7: 

			try: 
				income = float(item[55]) 
			except:
				income = 0 

			median_incomes[new_key] = income
			
		else:
			pass 

	print median_incomes   


def load_data(file):
	f = open(file) 
	reader = csv.reader(f)
	headers = reader.next() 
	
	co_name = headers.index('CONAME')
	co_add = headers.index('ADDR') 
	ct = headers.index('CENSUS_TRACT_2010') 
	cb = headers.index('CENSUS_BG_2010') 

	for business in reader:
		print business[ct], business[cb]


#	print "done in ", datetime.now() - startTime	
#['CONAME', 'ADDR', 'CITY', 'STATE', 'ZIP', 'INDFRM', 'PRMSIC', 'PRMSICD', 'PNACODE', 'PNATITL', 'EMPSDT', 'SLSVDT', 'HDBRCH', 'ABI', 'SUBNUM', 'ULTNUM', 'CENSUS_TRACT_2000', 'GE_CENSUS_BG_2000', 'CENSUS_TRACT_2010', 'CENSUS_BG_2010', 'LATITUDE_2010', 'LONGITUDE_2010']

if __name__=='__main__':
	startTime = datetime.now()
#	print startTime
	directory = os.environ['data_path']
	files = sorted(os.listdir(directory))
	df10 = directory + "/" + files[0] #make this dynamic at some point 
	load_MI_data("acs_MI.csv") 
