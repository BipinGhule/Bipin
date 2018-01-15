#Printing Stars in Reverse Angle Triangle Shape

def main():
	num = int(input("Enter the number vof rows"))
	for i in range(1,num+1):
		for j in range(num-i):
			print (" ",end=" "),
		for j in range(i):
			print ("*",end=" "),
		print("")
if __name__=='__main__':
	main()