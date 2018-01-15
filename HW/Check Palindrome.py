# Check Palindrome 
palin = raw_input("Enter any values:")

rev = palin[::-1]

if palin == rev:
	print "Input: {}, REV: {}".format(palin,rev)
	print "String is palindrome."
else:	
	print "Input: {}, REV: {}".format(palin,rev)
	print "String is  not palindrome."
	
Print "-----------------------------------------"	