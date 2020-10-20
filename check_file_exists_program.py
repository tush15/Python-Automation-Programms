import os
import sys

def fileexists(path):
	for dirname,subdirs,filelist in os.walk(path):
		for filen in filelist:
			if (filen == sys.argv[2]) :
				print ("file exists") 

			else:
				print ("file does not exists")	

def main():
	dir = sys.argv[1]
	fileexists(sys.argv[1]);

if __name__=="__main__":
	main();
