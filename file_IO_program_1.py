import os
import sys 

def filereading():
	f = open("Marvellous.txt",'r',encoding = 'utf-8')
			
	print(f.read())

	#f.close()

def main():
	filereading();

if __name__=="__main__":
	main()
