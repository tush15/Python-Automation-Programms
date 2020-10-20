import psutil

def Processdisplay():
	listprocess = []

	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid','name','username'])

			listprocess.append(pinfo);

		except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
			pass
	
	return listprocess

def main():
	print ("script by Tushar Parit ")

	print ("Process Moniter")

	listprocess = Processdisplay()

	for elem in listprocess:
		print (elem)

if __name__=="__main__":
	main();	

