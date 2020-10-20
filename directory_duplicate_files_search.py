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

def FindDuplicate(path): 
	flag = os.path.isabs(path)
	if flag == False :
		path = os.path.abspath(path)

	exists =os.path.isdir(path)

	dups = {}

	if exists:
		for dirs, subdirs, files in os.walk(path):
			print ("current folder is : " +  dirs )		
			for file in files:
				path = os.path.join(dirs,file)
				file_hash = hashfile(path)
				if file_hash in dups:
					dups[file_hash].append(path)
				else:
					dups[file_hash] =[path]
		return dups
	else :
		print ("invalid input")

def printduplicate(dict1):
	results = list(filter(lambda x:len(x) > 1, dict1.values()))

	if len(results) > 0:
		print ("duplicate founds")
	
	print ("the following files are identical.")

	icnt = 0
	for result in results:
		for subresult in result:
			icnt+=1
			if icnt>=2:
				print ('\t\t%s'% subresult)
	else:
		print ("No duplicate files found.")

def main():
	print("...script by Tushar Parit...")

	print("Application name: Directory duplicate file detector")

	if (len(sys.argv)!= 2):
		print("Error : Invalid number of arguments")

	if ((sys.argv[1])== "-h") or ((sys.argv[1])== "-H"):
		print("this script is used to travel specific directory and display checksum of files")

	if ((sys.argv[1])== "-u") or ((sys.argv[1])== "-U"):
		print("usage : Applicationname absolutepath_of_Directory Extension ")

	try : 
		arr = {}
		arr = FindDuplicate(sys.argv[1])
		printduplicate(arr)

	except ValueError :
		print("Error : invalid datatype of input")

	except Exception as E:
		print("Error : invalid input",E)

if __name__ == "__main__":
	main();
