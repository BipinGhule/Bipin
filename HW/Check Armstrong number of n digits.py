def Aramstrong():
	sum = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		sum += digit ** order
		temp //= 10

#	if num == sum:
#		print(num,"is an Armstrong number")
#	else:
#		print(num,"is not an Armstrong number")

def main():
	num = (input("Enter the number"))
	sum = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		sum += digit ** order
		temp //= 10
	if num == sum:
		print(num,"is an Armstrong number")
	else:
		print(num,"is not an Armstrong number")

	
if __name__=='__main__':
	main()




# num = 371
# #1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748
# # Changed num variable to string, 
# # and calculated the length (number of digits)
# order = len(str(num))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
   # digit = temp % 10
   # sum += digit ** order
   # temp //= 10

# # display the result
# if num == sum:
   # print(num,"is an Armstrong number")
# else:
   # print(num,"is not an Armstrong number")