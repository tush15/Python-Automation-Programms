import os
import sys 

def filereading():
	f = open (sys.argv[1],'r')
	p = f.read()
	f1 = open (sys.argv[2],'r')
	q = f1.read()
	if (p == q):
		print(" success ")
	else :
		print("failure") 
def main():
	filereading();

if __name__=="__main__":
	main();

