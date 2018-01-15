'''
def factorial(number):
	result  =1
	while (number != 1):
		result = result * number
		number -=1
	return result
def recursiveFactorial(number):
	if (number)

	
def main():
	num = eval(input("Enter the Number:"))
	print(factorial(num))


if __name__=='__main__':
	main()
	

	
def factorial(number):
	fact = -1
	if number > 0:
		if number <3:
			fact=number
		else:
			fact=1
			while number !=1:
				fact = fact*number
				number -=1
	print (fact)
	
if __name__=='__main__':
	factorial(5)
'''
def RecursiveFactorial(number):
	if number == 0 :
		return 1
	return	number * RecursiveFactorial(number-1)
print (RecursiveFactorial(5))


		
	
