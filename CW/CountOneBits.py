
def CountOneBits(no):
	x=1
	count=0
	while x<= no:
		if no & x !=0:
			count +=1
		x=x<<1
	return count

def main():
	num = eval(input("Enter the number:"))
	print (CountOneBits)
	
if __name__=='__main__':
	main()
	
#find negative number