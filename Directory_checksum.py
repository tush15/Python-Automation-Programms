import sys
import os
import hashlib

def hashfile(path , blocksize = 1024):
	afile = open(path,'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	afile.close()
	return hasher.hexdigest()

def DisplayChecksum(path): 
	flag = os.path.isabs(path)
	if flag == False :
		path = os.path.abspath(path)

	exists =os.path.isdir(path)
	if exists:
		for dirs, subdirs, files in os.walk(path):
			print ("current folder is : " +  dirs )		
			for file in files:
				path = os.path.join(dirs,file)
				file_hash = hashfile(path)
				print(path)
				print(file_hash)
				print('')
	else :
		print ("invalid input")

def main():
	print("...script by Tushar Parit...")

	print("Application name: directory checksum")

	if (len(sys.argv)!= 2):
		print("Error : Invalid number of arguments")

	if ((sys.argv[1])== "-h") or ((sys.argv[1])== "-H"):
		print("this script is used to travel specific directory and display checksum of files")

	if ((sys.argv[1])== "-u") or ((sys.argv[1])== "-U"):
		print("usage : Applicationname absolutepath_of_Directory Extension ")

	try : 
		arr = DisplayChecksum(sys.argv[1])
	
	except ValueError :
		print("Error : invalid datatype of input")

	except Exception as E:
		print("Error : invalid input",E)

if __name__ == "__main__":
	main();
