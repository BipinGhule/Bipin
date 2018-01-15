#Take in the upper range and lower range limit from the user.
#Take in the number to be divided by from the user.
#Using a for loop, print all the factors which is divisible by the number.
#Exit.

def main():
	lower=int(input("Enter lower range limit:"))
	upper=int(input("Enter upper range limit:"))
	n=(input("Enter the number to be multiple by:"))
	for i in range(lower,upper+1):
		if(i*n==0):
			print(i)
if __name__=='__main__':
	main()