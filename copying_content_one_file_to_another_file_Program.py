import os
import sys 

def filereading():
	f = open("abc.txt",'r',encoding = 'utf-8')
	p=f.read()
	f.close()
	f2 = open(sys.argv[1],'a')		
	f2.write(p)
	f2.close()
	f2 = open(sys.argv[1],'r')
	print(f2.read())
	f2.close()
def main():
	filereading();

if __name__=="__main__":
	main();
