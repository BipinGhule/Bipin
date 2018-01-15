'''
def FindGCD(no1,no2):
	if (no1 != no2):
		if no1 > no2):
			return FindGCD(no1-no2,no2)
		else:
			return	FindGCD(no1,no2-no1)
	else:
		return no1
	
def GCD(number):
	num1 = eval (input("Enter the number 1:"))
	num2 = eval (input ("Enter the number 2:"))
	print ("GCD of {},{} is :".format (no1,no2)+ str)findGCD(no1,no2)))
	
if __name__=='__main__':
	main()
'''	
def GCD (no1,no2):
	while (no1 != no2):
		if no1 > no2:
			no1 = no1-no2
		else:	
			no2 = no2-no1
	return no1
	
def main():
	no1,no2 = input ("Enter 2 number whose GCD is to be found:")
	result = GCD (no1,no2)
	print ("GCD of {},{} is{}".format(no1,no2,result))
	
if __name__=='__main__':
	main()
	
def RecursiveGCD(no1,no2):
	if no1==no2:
		return no1
	if no1 > no2:
		no1 -= no2
	else:
		no2 -1= no1
		
	return RecursiveGCD(no1,no2)
	