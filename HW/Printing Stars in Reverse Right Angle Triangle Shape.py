#Printing Stars in Reverse Right Angle Triangle Shape

def main():
	num = int(input("Enter the number vof rows"))
	for i in range(num,0,-1):
		for j in range(0,i):
			print( "*",end = " ")
		print()
if __name__=='__main__':
	main()