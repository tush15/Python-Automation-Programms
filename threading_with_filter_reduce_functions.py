import os;
import threading;
from functools import *;


arr=[34,45,56,67,78,89,74]
def chkeven(no):
	if ((no%2)==0):
		return True
	else:
		return False

def chkodd(no):
	if ((no%2)==1):
		return True
	else:
		return False

def sum(no1,no2):
	return no1+no2

def evenlist(no1):

	data=list(filter(chkeven,arr))
	
	brr=reduce(sum,data)
	print(brr)

	
def oddlist(no1):
	crr=list(filter(chkodd,arr))
	crr=reduce(sum,crr)
	print(crr)

def main():
	
	t1=threading.Thread(target=evenlist,args=(arr,))
	t2=threading.Thread(target=oddlist,args=(arr,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	

if __name__=="__main__":
	main();
