import os;
import threading;
from functools import * ;
no=[];
arr=[];
no1=int(input("no1 is"))
no2=int(input("no2 is"))

def even(no1):
	if ((no1%2)==0):
		return True
	else:
		return False
			
def odd(no2):
	if ((no2%2)==1):
		return True
	else:
		return False

def sum(no1,no2):
 	return no1+no2		
	
def adde(no1):
	data1=(even(no1))
	for i in range(2,no1):
		if ((no1%i)==0):
			for j in range(1):	
				if ((i%2)==0):
					no.append(i)
			
def addo(no2):
	data2=(odd(no2))
	for i in range (2,no2):
		if ((no2%i)==0):
			arr.append(i)
def evenlist(no1):
	a=adde(no1)
	print(no)	
	b=sum(no[0],no[1])
	print(b)

def oddlist(no2):
	a=addo(no2)
	print(arr)	
	c=sum(arr[0],arr[1])
	print(c)

def main():
	
	t1=threading.Thread(target=evenlist,args=(no1,))
	t2=threading.Thread(target=oddlist,args=(no2,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()
	
	print("exit from main")

if __name__=="__main__":
	main();
