import os;
import threading;

no1=int(input("no1 is"))
no2=int(input("no2 is"))

def fun(no1):
	for i in range(21):
		if ((i%2)==0):
			print (i)

def gun(no2):
	for i in range(20):
		if ((i%2)!=0):
			print (i)


def main():
	
	t1=threading.Thread(target=fun,args=(no1,))
	t2=threading.Thread(target=gun,args=(no2,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	

if __name__=="__main__":
	main();
