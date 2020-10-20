import sys
import os

def extension(directory):
	
	Directory = sys.argv[2]
	parent_dir = "/home/tushar/desktop/assignments"
	path = os.path.join(parent_dir, Directory) 			
	os.mkdir(path) 
	print("Directory '% s' created" % Directory) 
	for root, dirs, files in os.walk(directory):
		for file in files:
			true= file
			return true
def main():
	extension(sys.argv[1]);

if __name__ == "__main__":
	main();
