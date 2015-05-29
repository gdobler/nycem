import os 
import json
from urllib import urlopen 










if __name__=='__main__':
	directory = os.environ['data_path']
	files = sorted(os.listdir(directory))
	print files 
