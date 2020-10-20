import sys
import os

def extension(directory):
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith(sys.argv[2]):
				filename = (file)
				(prefix, sep, suffix) = filename.rpartition('.')
				new_filename = prefix + sys.argv[3]
				print (new_filename)
				

def main():
	extension(sys.argv[1]);

if __name__ == "__main__":
	main();
