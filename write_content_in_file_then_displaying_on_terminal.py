import os
import sys 

def filereading():
	p = len(sys.argv[2])
	f = open (sys.argv[1],'w')
	f.write(p)
	f1 = open (sys.argv[1],'r')
	print(f1.read())

def main():
	
	filereading();

if __name__=="__main__":
	main();

